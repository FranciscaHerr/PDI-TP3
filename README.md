# README - Detección de carriles 


## Descripción: 
Este proyecto implementa la detección automática de carriles en videos de una ruta utilizando técnicas de procesamiento de imágenes con las bibliotecas OpenCV y Numpy. Se procesan videos grabados con una cámara fija ubicada en el interior del auto, orientada hacia la carretera.


## Requisitos:
Python 
OpenCV
Numpy


Instala las dependencias utilizando pip:
pip install opencv-python numpy


## Archivos:

-> ruta_1.mp4: Primer video de la ruta.

-> ruta_2.mp4: Segundo video de la ruta.

-> video_con_lineas1.mp4: Resultado del primer video con las líneas detectadas.

-> video_con_lineas2.mp4: Resultado del segundo video con las líneas detectadas.


## Ejecución:
Para procesar los videos y generar los resultados, ejecuta el código de tp3_pdi.py.

import cv2
import numpy as np


## Procesar el video y guardar el resultado
procesar_video_con_lineas('ruta_1.mp4', 'video_con_lineas1.mp4')
procesar_video_con_lineas('ruta_2.mp4', 'video_con_lineas2.mp4')
