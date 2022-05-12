from psycopg2 import connection
from database.db import get_connection_db
from .entities.records import Record_List

class RecordModel():
    
    @classmethod
    def get_records(self):
        try:
            connection=get_connection_db()
            list_record=[]
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM records ")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    record = Record_List(row[0],row[1],row[3])
                    list_record.append(record)
            connection.close()
            return  list_record
        except Exception as ex:
            raise Exception(ex)