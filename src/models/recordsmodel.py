from email import message
from flask import jsonify
from pandas import json_normalize
from database.db import get_connection_read_records,get_conexion_save_dataframe
from .entities.records import Record_List
from .entities.ent_get_ubication import Get_Ubication_by_ID


class RecordModel():
    
    @classmethod
    def get_records(self):
        try:
            connection=get_connection_read_records()
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
                    print(type(row))
                    record = Record_List(row[0],row[1],row[2],row[3],row[4])
                    list_record.append(record.to_JSON())
            connection.close()
           
            return  list_record
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_records_for_id(self,id):
        
            mysql_query ="""SELECT  RD.vehicle_id,RD.geographic_point,UT.postal_code,UT.country_code,UT.community_name,UT.state_name,UT.road,UT.community_name,UT.neighbourhood,UT.highway,UT.place_name,UT.alcaldia_name
	                    FROM records AS RD INNER JOIN ubication as UT ON RD.vehicle_id=UT.vehicle_id 
                        WHERE RD.vehicle_id={}""".format(id)
                 
           
            try:
                connection=get_conexion_save_dataframe()
                rowrecord= connection.execute(mysql_query).fetchone()
               # print(rowrecord)                                              
                record=Get_Ubication_by_ID(rowrecord[0],rowrecord[1],rowrecord[2],rowrecord[2],rowrecord[3],rowrecord[4],rowrecord[5],rowrecord[6],rowrecord[7],rowrecord[8],rowrecord[9])
                # print(record)
                # print(record.to_JSON() )       
                return record.to_JSON()
            except Exception as ex:
                raise Exception(ex)