import torch
import cv2
import numpy as np
import pandas as pd
import pytesseract
from pytesseract import Output
import easyocr
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

def loadModel(data_input):
    data_input = str(data_input)
    reader = easyocr.Reader(["es"], gpu=True)
    # Leemos el modelo
    model = torch.hub.load('C:/Users/daft1/OneDrive/Escritorio/respaldo/RPA CORELMEX DNA/YOLO/yolov7/CustomMODEL/WongKinYiu-yolov7-3b41c2c', 'custom',
                           'C:/Users/daft1/OneDrive/Escritorio/respaldo/RPA CORELMEX DNA/YOLO/yolov7/runs/train/yolov7-custom/weights/best.pt', source='local', force_reload=True)
    
    img = data_input
    results = model(img)

    Dataframe = results.pandas().xyxy[0]
    fila_nombre = Dataframe.loc[Dataframe['class'] == 0]
    print("DATAFRAME: ", Dataframe)
    fila_direccion = Dataframe.loc[Dataframe['class'] == 1]
    fila_clave = Dataframe.loc[Dataframe['class'] == 2]
    fila_curp = Dataframe.loc[Dataframe['class'] == 3]
    fila_anho = Dataframe.loc[Dataframe['class'] == 4]
    fila_fecha = Dataframe.loc[Dataframe['class'] == 5]
    fila_genero = Dataframe.loc[Dataframe['class'] == 6]
    fila_vigencia = Dataframe.loc[Dataframe['class'] == 7]

    ori = cv2.imread(img)
    imagen = cv2.imread(img)
    detect = model(imagen)
    info = detect.pandas().xyxy[0]
    
    #recortes
    print("ORIGINAL ", fila_fecha['ymin'])
    print("ORIGINAL 444", fila_fecha)
    RecorteNombreImagen = ori[int(fila_nombre['ymin']):int(fila_nombre['ymax']), int(fila_nombre['xmin']):int(fila_nombre['xmax']), :]
    RecorteDireccionImagen = ori[int(fila_direccion['ymin']):int(fila_direccion['ymax']), int(fila_direccion['xmin']):int(fila_direccion['xmax']), :]
    RecorteClaveImagen = ori[int(fila_clave['ymin']):int(fila_clave['ymax']), int(fila_clave['xmin']):int(fila_clave['xmax']), :]
    RecorteCurpImagen = ori[int(fila_curp['ymin']):int(fila_curp['ymax']), int(fila_curp['xmin']):int(fila_curp['xmax']), :]
    RecorteAnhoImagen = ori[int(fila_anho['ymin']):int(fila_anho['ymax']), int(fila_anho['xmin']):int(fila_anho['xmax']), :]
    #RecorteFechaImagen = ori[int(fila_fecha['ymin']):int(fila_fecha['ymax']), int(fila_fecha['xmin']):int(fila_fecha['xmax']), :]
    #RecorteGeneroImagen = ori[int(fila_genero['ymin']):int(fila_genero['ymax']), int(fila_genero['xmin']):int(fila_genero['xmax']), :]
    RecorteVigenciaImagen = ori[int(fila_vigencia['ymin']):int(fila_vigencia['ymax']), int(fila_vigencia['xmin']):int(fila_vigencia['xmax']), :]
    Nombre = str(pytesseract.image_to_string(RecorteNombreImagen, config='--oem 3 --psm 6')).replace("\n", " ").replace("NOMBRE", "").replace(" > ", "")
    Direccion = str(pytesseract.image_to_string(RecorteDireccionImagen, config='--oem 3 --psm 6')).replace("\n", " ").replace("DOMICILIO", "").replace("- . 7 _ - ", "")
    Clave = str(pytesseract.image_to_string(RecorteClaveImagen, config='--oem 3 --psm 6')).replace("\n", " ").replace("D CLAVEDEELECTOR ", "")
    Curp = str(pytesseract.image_to_string(RecorteCurpImagen, config='--oem 3 --psm 6')).replace("\n", " ").replace("CURP. ", "").replace("- ", "")
    Anho = str(pytesseract.image_to_string(RecorteAnhoImagen, config='--oem 3 --psm 6')).replace("\n", " ").replace("ARO DE REGISTRO ", "")
    #Fecha = str(pytesseract.image_to_string(RecorteFechaImagen, config='--oem 1 --psm 4')).replace("\n", " ").replace("FECHA DE NACIMIENTO", "")
    #Genero = str(pytesseract.image_to_string(RecorteGeneroImagen, config='--oem 1 --psm 4')).replace("\n", " ").replace("Sexo ", "")
    Vigencia = str(pytesseract.image_to_string(RecorteVigenciaImagen, config='--oem 3 --psm 6')).replace("\n", " ").replace("VIGENCIA ", "").replace(",~", "-").replace(" ", "")
    # ZONA LECTURA
    cv2.imshow('Completa', np.squeeze(detect.render()))
    cv2.imshow('Nombre', RecorteNombreImagen)
    cv2.imshow('Direccion', RecorteDireccionImagen)
    cv2.imshow('Clave', RecorteClaveImagen)
    cv2.imshow('Curp', RecorteCurpImagen)
    cv2.imshow('Anho', RecorteAnhoImagen)
    #cv2.imshow('Fecha', RecorteFechaImagen)
    #cv2.imshow('Genero', RecorteGeneroImagen)
    cv2.imshow('Vigencia', RecorteVigenciaImagen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return Nombre, Direccion, Clave, Curp, Anho, Vigencia