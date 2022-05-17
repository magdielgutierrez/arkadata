from traceback import print_tb
from flask import Blueprint, jsonify
from sqlalchemy import null
# Models
from models.recordsmodel import RecordModel

main = Blueprint('list_records',__name__)

@main.route('/')
def get_records():
    try:

        list_of_records = RecordModel.get_records()
        return jsonify(list_of_records)
    except Exception as ex:
        return jsonify({'message':'Hola tenemos un error'})
 
@main.route('/<id>')
def get_ubication_for_id(id):
    try:
        ubication_id = RecordModel.get_records_for_id(id)
        if ubication_id == None:
            return jsonify({}),404
        else:
            return jsonify(ubication_id)
    except Exception as ex:
        return jsonify({'message':'Hola no podemos obtener una ubicacion'}),500

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

@main.route('/municipal')
def get_mayors_available():
    try:
        list_mayors= RecordModel.get_list_of_municipal_available()
        if list_mayors == None:
            return jsonify({}),404
        else:
            return jsonify(list_mayors)
    except Exception as ex:
        return jsonify({'message':'Hola no hay alcaldias disponibles'}),500
    

@main.route('/search/<name>')
def get_municipal_units(name):
    try:
        municipal_units= RecordModel.get_list_of_municipal_units(name)
        if municipal_units == None:
            return jsonify({}),404
        else:
            return jsonify(municipal_units)
    except Exception as ex:
        return jsonify({'message':'Hola no hay unidades en la alcaldia'}),500
    
