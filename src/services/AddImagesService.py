from flask import request, jsonify
# Database
from src.database.database import get_connection
# Errors
from src.utils.errors.CustomException import CustomException
# Models 
from src.models.Images import Images


class AddImagesService():

    @classmethod
    def add_images(cls, images):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                ##########################################################nombre, pathDirection, pathDirection, estatus, tipo_documento, tramite
                ##########################################################(pNombre, pImagen, pRuta, pEstatus_documento, pTipo_documento, pTramite)
                cursor.execute('call sp_addImageProc(%s, %s)', (images.usuario, images.path_direction))
                resultSet = cursor.fetchall()
            connection.commit()
            connection.close()
            return jsonify({"Execute success ": resultSet})
        except CustomException as ex:
            raise CustomException(ex)