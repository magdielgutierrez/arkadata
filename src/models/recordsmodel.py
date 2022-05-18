from email import message
from flask import jsonify
from pandas import json_normalize
from database.db import get_conexion_mysql
from .entities.record_value_to_json import *

class RecordModel():
    
    # search with select all records and return JSON 
    @classmethod 
    def get_all_records(self):
            list_units=[]
            mysql_query ="""SELECT id,date_updated,vehicle_id,vehicle_label, vehicle_status,vehicle_id
                                    geographic_point,position_odometer,position_speed
                                  FROM records """
           
            try:
                connection=get_conexion_mysql()
                resultset= connection.execute(mysql_query).fetchall()  
                
                for row in resultset:
                    units=get_all_records(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                    list_units.append(units.to_JSON())
                
                return list_units
            
            except Exception as ex:
                raise Exception(ex)
            
    # search with select  location for ID  and return JSON    
    @classmethod
    def get_ubication_for_id(self,id):
        
            mysql_query ="""SELECT  RD.vehicle_id,RD.geographic_point,UT.postal_code,UT.country_code,UT.community_name,UT.state_name,UT.road,UT.community_name,UT.neighbourhood,UT.highway,UT.place_name,UT.alcaldia_name
	                    FROM records AS RD INNER JOIN ubication as UT ON RD.vehicle_id=UT.vehicle_id 
                        WHERE RD.vehicle_id={}""".format(id)
                 
            try:
                connection=get_conexion_mysql()
                rowrecord= connection.execute(mysql_query).fetchone()                                            
                record=get_unit_location_by_id(rowrecord[0],rowrecord[1],rowrecord[2],rowrecord[2],rowrecord[3],rowrecord[4],rowrecord[5],rowrecord[6],rowrecord[7],rowrecord[8],rowrecord[9])
                return record.to_JSON()
            except Exception as ex:
                raise Exception(ex)
          
    # search list avalibale units and return JSON 
    @classmethod
    def get_list_of_available_units(self):
            list_units=[]
            mysql_query ="SELECT vehicle_id FROM records WHERE vehicle_status=1"
           
            try:
                connection=get_conexion_mysql()
                resultset= connection.execute(mysql_query).fetchall()  
                
                for row in resultset:
                    units=get_available_units(row[0])
                    list_units.append(units.to_JSON())
                    
                return list_units
            
            except Exception as ex:
                raise Exception(ex)
            
    # search list mayors and return JSON 
    @classmethod
    def get_list_of_municipal_available(self):
        
            mysql_query ="SELECT alcaldia_name FROM ubication WHERE alcaldia_name IS NOT NULL GROUP BY alcaldia_name"     
            list_mayors=[]

            try:
                connection=get_conexion_mysql()
                result= connection.execute(mysql_query).fetchall()  
                
                for row in result:
                    mayors=get_municipal_available(row[0])
                    list_mayors.append(mayors.to_JSON())
                    
                return list_mayors
            
            except Exception as ex:
                raise Exception(ex)
            
     # search list avalibale units by mayors and return JSON        
    @classmethod
    def get_list_of_municipal_units(self,name):
        
            mysql_query ="""SELECT records.vehicle_id FROM records INNER JOIN ubication ON records.vehicle_id=ubication.vehicle_id
                        WHERE ubication.alcaldia_name='{}'""".format(name)    
            list_units=[]
            
            try:
                connection=get_conexion_mysql()
                result= connection.execute(mysql_query).fetchall()  
                
                for row in result:
                    units=get_municipal_units(row[0])
                    list_units.append(units.to_JSON())
                    
                return list_units
            
            except Exception as ex:
                raise Exception(ex)
                     