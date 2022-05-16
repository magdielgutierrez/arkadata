from database.db import get_connection_db
from .entities.records import Record_List
class RecordModel():
    
    @classmethod
    def get_records(self):
        try:
            connection=get_connection_db()
            list_record=[]
            
            with connection.cursor() as cursor:
                cursor.execute("""SELECT id,date_updated,vehicle_id,vehicle_label, vehicle_status,vehicle_id
                                    geographic_point,position_odometer,position_speed
                                  FROM records """)
                resultset=cursor.fetchall()
                # print('\n')
                # print('\n')
                #print( resultset)
                # print(type(resultset))
                # print('\n')
                # print('\n')
                
                for row in resultset:
                    print(type(row))
                    record = Record_List(row[0],row[1],row[2],row[3],row[4])
                    list_record.append(record.to_JSON())
            connection.close()
           
            return  list_record
        except Exception as ex:
            raise Exception(ex)