
# ---->> librerias
from flask import request, jsonify
# ---->> cargamos las funcionalidades de la base de datos
from src.database.database import get_connection
# ---->> importamos la funcionalidad de errors
from src.utils.errors.CustomException import CustomException

class DetectionOCRService():

    @classmethod
    def detection_ocr_service(self, Nombre, Direccion, Clave, Curp, Anho, Vigencia):
        try:
            self.Nombre = Nombre
            self.Direccion = Direccion
            self.Clave = Clave
            self.Curp = Curp
            self.Anho = Anho
            self.Vigencia = Vigencia
            Ruta = "REFEr"
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('INSERT INTO tbl_data_extracted(anho, clave, curp, direccion, nombre, vigencia, ruta) VALUES(%s, %s, %s, %s, %s, %s, %s)', (Anho, Clave, Curp, Direccion, Nombre, Vigencia, Ruta))
                resultInsertInfo = cursor.fetchall()
            connection.commit()
            connection.close()
            return jsonify({"executeSuccess": resultInsertInfo})
        except CustomException as ex:
            raise CustomException(ex)