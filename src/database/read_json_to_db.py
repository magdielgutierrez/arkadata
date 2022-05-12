import json
import pandas as pd 


# Opening JSON file
file_json = open('data.json')

# returns JSON object as dictionary
dict_data = json.load(file_json)

for key, value in dict_data.items():
    list_result = dict_data["result"]

for key, value in list_result.items():
    list_records = list_result["records"]


list_data={"id":[],
            "date_updated":[],
            "vehicle_id":[],
            "vehicle_label":[],
            "vehicle_status":[],
            "geographic_point":[],
            "position_odometer":[],
            "position_speed":[]}

for record in list_records:
    for key,value in record.items():   
 #       print(key,"--",value,"\n")
        if key == "id":                 
            list_data['id'].append(value)

        if key == "date_updated":                 
            list_data['date_updated'].append(value)

        if key == "vehicle_id":                 
            list_data['vehicle_id'].append(value)

        if key == "vehicle_label":                 
            list_data['vehicle_label'].append(value)

        if key == "vehicle_current_status":                 
            list_data['vehicle_status'].append(value)
        
        if key == "geographic_point":                 
            list_data['geographic_point'].append(value)

        if key == "position_odometer":                 
            list_data['position_odometer'].append(value)

        if key == "position_speed":                 
            list_data['position_speed'].append(value)

df_raw_data = pd.DataFrame.from_dict(list_data,orient='index')
df_end_data = df_raw_data.T
print(df_end_data)

# # Closing file
file_json.close()

