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
                # print( resultset)
                # print(type(resultset))
                # print('\n')
                # print('\n')
                
                for row in resultset:
                    row0=row[0]
                    row1=row[1]
                    row2=row[2]
                    row3=row[3]
                    row4=row[4]
                    row5=row[5]
                    row6=row[6]
                    row7=row[7]
                   # record = Record_List(row0,row1,row2,row3,row4,row5,row6,row7)
                    record = Record_List(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row7)
                   # print("tipo devulve record_lst",type(record))
                    list_record.append(record.to_JSON())
            connection.close()
            #print(list_record)
            return  list_record
        except Exception as ex:
            raise Exception(ex)