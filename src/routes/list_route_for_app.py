from email import message
from traceback import print_tb
from flask import Blueprint, jsonify
from sqlalchemy import null
from utils.validaciones import *
from database.db import get_conexion_mysql

# Models
from models.recordsmodel import RecordModel

main = Blueprint('list_records',__name__)

# Principal route
@main.route('/')
def get_home():
        return jsonify({'message':'Enhorabuena.. estas en el REST API de ArkaData'})
 
 # List all records
@main.route('/list')
def get_records():
    try:

        list_of_records = RecordModel.get_all_records()
        return jsonify(list_of_records)
    except Exception as ex:
        return jsonify({'message':'Hola no encontramos ningun registros'}),500
 
 # Get unit location by ID
@main.route('/<id>')
def get_ubication_for_id(id):
    
    if validar_id_unidad(id):
        
            try:
                ubication_id = RecordModel.get_ubication_for_id(id)
                if ubication_id == None:
                    return jsonify({}),404
                else:
                    return jsonify(ubication_id)
            except Exception as ex:
                return jsonify({'message':'Hola no podemos obtener una ubicacion'}),500
    else: return jsonify({'mensaje': "Parámetros inválidos...", 'Action': False})
    
# Get available units
@main.route('/units')
def get_available_units():
    try:
        list_available = RecordModel.get_list_of_available_units()
        if list_available == None:
            return jsonify({}),404
        else:
            return jsonify(list_available)
    except Exception as ex:
        return jsonify({'message':'No tenemos unidades disponibles en este momento'}),500

# Get  list of mayors
@main.route('/municipal')
def get_municipal_available():
    
    try:
        list_mayors= RecordModel.get_list_of_municipal_available()
        if list_mayors == None:
            return jsonify({}),404
        else:
            return jsonify(list_mayors)
    except Exception as ex:
        return jsonify({'message':'Hola no hay alcaldias disponibles'}),500
   
# Get List units by mayor
@main.route('/search/<name>')
def get_municipal_units(name):
    
      if validar_nombre_alcaldia(name) and validar_tipo_nombre_alcaldia(name)==False:
        try:
            municipal_units= RecordModel.get_list_of_municipal_units(name)
            if municipal_units == None:
                return jsonify({}),404
            else:
                return jsonify(municipal_units)
        except Exception as ex:
            return jsonify({'message':'Hola no hay unidades en la alcaldia'}),500
      else: return jsonify({'mensaje': "Parámetros inválidos...", 'Action': False})


# Get  conexion db
@main.route('/db')
def get_cxn_db_message():
    msg= get_conexion_mysql()
    return jsonify({'message': '{}'.format(msg)})
    
   