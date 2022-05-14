import json
import pandas as pd 
import simplejson as json
import pgeocode
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
data = pgeocode.Nominatim('MX')


# Opening JSON file
file_json = open('./data.json')

# returns JSON object as dictionary
dict_data = json.load(file_json)

for key, value in dict_data.items():
    list_result = dict_data["result"]

for key, value in list_result.items():
    list_records = list_result["records"]


dict_table_records={"id":[],"date_updated":[],"vehicle_id":[],
                    "vehicle_label":[],"vehicle_status":[],"geographic_point":[],
                    "position_odometer":[],"position_speed":[]}

dict_table_ubication={"vehicle_id":[],"postal_code":[],"alcaldia_name":[],
                    "highway":[],"road":[],"neighbourhood":[] }

list_geographic_point=[]

df_list_Value_codezip=pd.DataFrame(dtype = 'object')

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
            list_geographic_point.append(value)
           
        if key == "position_odometer":                 
            dict_table_records['position_odometer'].append(value)

        if key == "position_speed":                 
            dict_table_records['position_speed'].append(value)


# #pass dict_table_records to df_raw_table_records
# df_raw_table_records = pd.DataFrame.from_dict(dict_table_records,orient='index')
# df_raw_table_records = df_raw_table_records.T
# print(df_raw_table_records)

count = 0
for point in list_geographic_point:
    
    if count < 2:
        location = geolocator.reverse(point)
        address = location.raw['address']
        #print("\n",type(address))
        for key,value in address.items(): 
            #print(key," -- ", value,"\n")
            if key == "postcode":                 
                dict_table_ubication['postal_code'].append(value)
                serie_for_search_code= data.query_postal_code(value)
                df_for_search_code = serie_for_search_code.to_frame()               
                df_for_search_code=df_for_search_code.T
                df_for_search_code.drop(columns=['accuracy','latitude','longitude'],inplace=True)
                
                #concat df_list_Value_codezip +  df_for_search_code 
                df_list_Value_codezip = pd.concat([df_list_Value_codezip, df_for_search_code], ignore_index = True, axis = 0)
                                    
            if key == "highway":                 
                dict_table_ubication['highway'].append(value)

            if key == "road":                 
                dict_table_ubication['road'].append(value)

            if key == "neighbourhood":                 
                dict_table_ubication['neighbourhood'].append(value)

  
        
        
        count+=1
    else:break

#print(df_list_Value_codezip)

#pass dict_table_ubication to df_raw_table_ubication
df_raw_table_ubication = pd.DataFrame.from_dict(dict_table_ubication,orient='index')
df_raw_table_ubication=df_raw_table_ubication.T
#print(df_raw_table_ubication)

df_table_ubication= df_raw_table_ubication.merge(df_list_Value_codezip, on='postal_code')
print(df_table_ubication)

df_table_ubication.info(verbose=True)


# # Closing file
file_json.close()

