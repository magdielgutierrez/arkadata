from flask import Blueprint, jsonify
# Models
from models.recordsmodel import RecordModel

main = Blueprint('list_records',__name__)

@main.route('/')
def get_records():
    try:
        list_of_records = RecordModel.get_records()
        return list_of_records
        pass
    except Exception as ex:
        return jsonify({'message':'Hola'})