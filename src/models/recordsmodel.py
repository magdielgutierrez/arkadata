from email import message
from flask import jsonify
from pandas import json_normalize
from database.db import get_connection_read_records,get_conexion_save_dataframe
from .entities.records import Record_List
from .entities.record_value_to_json import get_unit_location_by_id,get_available_units,get_municipal_available,get_municipal_units



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
                record=get_unit_location_by_id(rowrecord[0],rowrecord[1],rowrecord[2],rowrecord[2],rowrecord[3],rowrecord[4],rowrecord[5],rowrecord[6],rowrecord[7],rowrecord[8],rowrecord[9])
                return record.to_JSON()
            except Exception as ex:
                raise Exception(ex)
            
    @classmethod
    def get_list_of_available_units(self):
            list_units=[]
            mysql_query ="SELECT vehicle_id FROM records WHERE vehicle_status=1"
           
            try:
                connection=get_conexion_save_dataframe()
                resultset= connection.execute(mysql_query).fetchall()  
                
                for row in resultset:
                    units=get_available_units(row[0])
                    list_units.append(units.to_JSON())
                    
                return list_units
            
            except Exception as ex:
                raise Exception(ex)
            
    @classmethod
    def get_list_of_municipal_available(self):
        
            mysql_query ="SELECT alcaldia_name FROM ubication WHERE alcaldia_name IS NOT NULL GROUP BY alcaldia_name"     
            list_mayors=[]

            try:
                connection=get_conexion_save_dataframe()
                result= connection.execute(mysql_query).fetchall()  
                
                for row in result:
                    mayors=get_municipal_available(row[0])
                    list_mayors.append(mayors.to_JSON())
                    
                return list_mayors
            
            except Exception as ex:
                raise Exception(ex)
            
            
    @classmethod
    def get_list_of_municipal_units(self,name):
        
            mysql_query ="""SELECT records.vehicle_id FROM records INNER JOIN ubication ON records.vehicle_id=ubication.vehicle_id
                        WHERE ubication.alcaldia_name='{}'""".format(name)    
            list_units=[]
            print('Hola mundo nuevamente')
            try:
                connection=get_conexion_save_dataframe()
                result= connection.execute(mysql_query).fetchall()  
                
                for row in result:
                    units=get_municipal_units(row[0])
                    list_units.append(units.to_JSON())
                    
                return list_units
            
            except Exception as ex:
                raise Exception(ex)
                     