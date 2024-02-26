from flask import Blueprint, request, jsonify
# Models
from src.models.Images import Images
# Security
from src.utils.Security import Security
# Services
from src.services.AddImagesService import AddImagesService


main = Blueprint('images_blueprint', __name__)

@main.route('/', methods = ['POST'])
def add():
    has_access =  Security.verify_token(request.headers)
    print(has_access)
    usuario = request.json['usuario']
    pathDirection = request.json['pathdirection'] # esta sirve tanto para image como para ruta
    if has_access:
        _images = Images(usuario, pathDirection) 
        resultSet = AddImagesService.add_images(_images)
        return jsonify({'success query ': "agregado de imagen correcta", "messege": str(resultSet)})
    else:
        response = jsonify({'message': 'Unauthorized'})
        return response, 401,