
# ---->> librerias 
from flask import Blueprint, request, jsonify
# ---->> importamos la funcionalidad errors
from src.utils.errors.CustomException import CustomException
# ---->> importamos la funcionalidad de security
from src.utils.Security import Security
# ---->> importamos la funcionalidad de services
from src.services.DetectionOCRService import DetectionOCRService
# ---->> importamos la funcionalidad de despliegue de modelo convolucional
from src.utils.controllers.centralNeuralNetwork import loadModel


main = Blueprint('ocr_blueprint', __name__)

@main.route('/', methods = ['POST'])
def detection_ocr():
    has_access = Security.verify_token(request.headers)
    if has_access:
        data_input = request.json['path']
        Nombre, Direccion, Clave, Curp, Anho, Vigencia = loadModel(data_input)

        resultInsertInfo = DetectionOCRService.detection_ocr_service(Nombre, Direccion, Clave, Curp, Anho, Vigencia)
        return jsonify({"successQuery": "Se analizo imagen de manera correcta",
                        "message": str(resultInsertInfo),
                        "nombre": Nombre,
                        "direccion": Direccion,
                        "clave": Clave,
                        "curp": Curp,
                        "anho": Anho,
                        "vigencia": Vigencia})
    else:
        response = jsonify({"message": "Unauthorized"})
        return response, 401
    