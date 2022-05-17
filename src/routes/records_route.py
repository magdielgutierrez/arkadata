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
        return jsonify({'message':'Hola tenemos un error para obtener la ubicacion'}),500