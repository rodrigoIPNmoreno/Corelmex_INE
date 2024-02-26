from flask import Blueprint, request, jsonify

# Models
from src.models.Info import Info
# Security 
from src.utils.Security import Security
# Services
from src.services.ShowInfoService import ShowInfoService

main = Blueprint('information_blueprint', __name__)

@main.route('/', methods = ['GET'])
def show():
    has_access = Security.verify_token(request.headers)
    if has_access:
        _info = Info()
        resultRequest = ShowInfoService()
        return jsonify({'petition success ': "acceso a pagina de infomacion completada", "messege": str(resultRequest)})
    else:
        response = jsonify({"messege":"Unauthorized"})
        return response, 401