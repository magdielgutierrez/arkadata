import json
import pandas as pd 
import simplejson as json
import pgeocode
import time
from geopy.geocoders import Nominatim

from db import get_conexion_mysql


from sqlalchemy import create_engine

geolocator = Nominatim(user_agent="geoapiExercises")
data = pgeocode.Nominatim('MX')
engine_cnxn_save_dataframe = get_conexion_mysql()

# Define  dict_table_records base for table  records in database
dict_table_records={"id":[],"date_updated":[],"vehicle_id":[],
                        "vehicle_label":[],"vehicle_status":[],"geographic_point":[],
                        "position_odometer":[],"position_speed":[]}

# Define  dict_table_ubication base for table  ubication in database
dict_table_ubication={"vehicle_id":[],"postal_code":[],"highway":[],
                        "road":[],"neighbourhood":[] }

# List receiving geographic_point values by search ubication
list_geographic_point=[]

    # Inicialize Dataframe , receive postal code values series
df_list_value_codezip=pd.DataFrame(dtype = 'object')

def read_json_file():
      # Opening JSON file
    file_json = open('./data.json')
    return  json.load(file_json)

    
def save_records_to_table_records(dict_data_records, list_geographic_point):
    # Select key by create new list_result and list_records
    for key, value in dict_data_records.items():
        list_result = dict_data_records["result"]

    for key, value in list_result.items():
        list_records = list_result["records"]

    # Action by create dict_table_records using dict_data JSON 
    for record in list_records:
        for key,value in record.items():   
            if key == "id":                 
                dict_table_records['id'].append(value)

            if key == "date_updated":                 
                dict_table_records['date_updated'].append(value)

            if key == "vehicle_id":                 
                dict_table_records['vehicle_id'].append(value)
                dict_table_ubication['vehicle_id'].append(value)

            if key == "vehicle_label":                 
                dict_table_records['vehicle_label'].append(value)

            if key == "vehicle_current_status":                 
                dict_table_records['vehicle_status'].append(value)
            
            if key == "geographic_point":                 
                dict_table_records['geographic_point'].append(value)
               # if len(value) > 20: list_geographic_point.append(value)
                list_geographic_point.append(value)
            
            if key == "position_odometer":                 
                dict_table_records['position_odometer'].append(value)

            if key == "position_speed":                 
                dict_table_records['position_speed'].append(value)


    # Pass dict_table_records to df_raw_table_records
    df_raw_table_records = pd.DataFrame.from_dict(dict_table_records,orient='index')
    df_raw_table_records = df_raw_table_records.T
    # print(df_raw_table_records.head(5))
    # print(df_raw_table_records.info())
    return df_raw_table_records

def save_records_to_table_ubication(list_geographic_point,df_list_value_codezip):

        for point in list_geographic_point:
            if len(point)>20 :
                location = geolocator.reverse(point)
                address = location.raw['address']
                time.sleep(0.2)

                for key,value in address.items(): 
                    #print(key," -- ", value,"\n")
                    if key == "postcode":                          
                        dict_table_ubication['postal_code'].append(value)
                        serie_for_search_code= data.query_postal_code(value)
                        df_for_search_code = serie_for_search_code.to_frame()               
                        df_for_search_code=df_for_search_code.T
                        
                        df_for_search_code.drop(columns=['accuracy','latitude','longitude'],inplace=True)
                                                
                        #concat df_list_Value_codezip +  df_for_search_code 
                        df_list_value_codezip = pd.concat([df_list_value_codezip, df_for_search_code], ignore_index = True, axis = 0)                   
                    if key == "highway":                 
                        dict_table_ubication['highway'].append(value)

                    if key == "road":                 
                        dict_table_ubication['road'].append(value)

                    if key == "neighbourhood":                 
                        dict_table_ubication['neighbourhood'].append(value)            

        # #Pass dict_table_ubication to df_raw_table_ubication
        df_raw_table_ubication = pd.DataFrame.from_dict(dict_table_ubication,orient='index')
        df_raw_table_ubication=df_raw_table_ubication.T


        df_table_ubication= df_raw_table_ubication.merge(df_list_value_codezip, on='postal_code',how='right')
        df_table_ubication.rename(columns = {'county_name':'alcaldia_name'}, inplace = True)
        df_table_ubication= df_table_ubication.drop_duplicates()
        return df_table_ubication


if __name__ == '__main__':
      
    # returns JSON object as dictionary
    dict_data_records = read_json_file()
    
    # read record from API  save to db MYSQL
    table_records= save_records_to_table_records(dict_data_records,list_geographic_point)
   
    if table_records.shape[0] > 0:
           # table_records.to_sql('records', con=engine_cnxn_save_dataframe, if_exists ='append', index=False) 
            print('¡Enhorabuena!.Haz ingresado {} registros nuevos.'.format(table_records.shape[0]) )
    else:
           print( '¡Ups!. No hemos encontrados registros nuevos...!')
       
    # #save record ubication to db MYSQL 
    table_ubication =save_records_to_table_ubication(list_geographic_point,df_list_value_codezip)


    if table_ubication.shape[0] > 0:
            #table_ubication.to_sql('ubication', con=engine_cnxn_save_dataframe, if_exists ='append', index=False) 
            print('¡Enhorabuena!.Haz ingresado {} registros nuevos.'.format(table_ubication.shape[0]) )
    else:
           print( '¡Ups!. No hemos encontrados registros nuevos...!')
    