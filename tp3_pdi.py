import cv2
import numpy as np

### FUNCIONES ########################################################################################################
def mask(frame):
    # Dimensiones de la imagen
    altura, anchura = frame.shape[:2]
    # Crear una máscara con la misma dimensión que la imagen y tipo uint8
    mascara = np.zeros((altura, anchura), dtype=np.uint8)
    # Definir los puntos del polígono
    puntos = np.array([[0, 0], [0, altura], [int(anchura * 0.47), int(altura * 0.6)], [int(anchura * 0.55), int(altura * 0.6)], [anchura, altura], [anchura, 0]])    
    # Rellenar el polígono con blanco en la máscara
    cv2.fillPoly(mascara, [puntos], 255)
    # Convertir la máscara a 3 canales
    mascara_color = cv2.cvtColor(mascara, cv2.COLOR_GRAY2BGR)
    # Aplicar la máscara para oscurecer la región
    frame_mascara = frame.copy()
    frame_mascara[mascara_color == 255] = 0
    # Convertir la imagen a escala de grises y aplicar umbral
    imagen_gris = cv2.cvtColor(frame_mascara, cv2.COLOR_BGR2GRAY)
    _, imagen_binaria = cv2.threshold(imagen_gris, 190, 255, cv2.THRESH_BINARY)
    return imagen_binaria

def procesar_video_con_lineas(archivo, salida):
    cap = cv2.VideoCapture(archivo)  
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    out = cv2.VideoWriter(salida, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Parámetros para la transformada de Hough
    rho = 1  # Resolución de rho en píxeles
    theta = np.pi / 180  # Resolución de theta en radianes
    threshold = 50  # Número mínimo de intersecciones para detectar una línea

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Aplicar máscara a cada frame
        imagen_mascara = mask(frame)

        # Detectar líneas
        lineas = cv2.HoughLinesP(imagen_mascara, rho, theta, threshold, np.array([]), minLineLength=50, maxLineGap=200)

        # Filtrar las líneas horizontales
        lineas_filtradas = []
        if lineas is not None:
            for linea in lineas:
                for x1, y1, x2, y2 in linea:
                    angulo = np.arctan2(y2 - y1, x2 - x1)
                    if not (-np.pi/8 < angulo < np.pi/8):  # Ajustar el umbral para definir qué es horizontal
                        lineas_filtradas.append([[x1, y1, x2, y2]])

        # Dibujar líneas en el frame original
        frame_con_lineas = frame.copy()
        if lineas is not None:
            for linea in lineas_filtradas:
                x1, y1, x2, y2 = linea[0]
                cv2.line(frame_con_lineas, (x1, y1), (x2, y2), (255, 0, 0), 3)

        out.write(frame_con_lineas)
        cv2.imshow('Frame con líneas detectadas', frame_con_lineas)
        #cv2.imshow('Frame con líneas detectadas', imagen_mascara)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

### DESARROLLO  ###########################################################################################################

# Procesar el video y guardar el resultado
procesar_video_con_lineas('ruta_1.mp4', 'video_con_lineas1.mp4')
