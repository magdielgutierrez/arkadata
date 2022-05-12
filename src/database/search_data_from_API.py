import urllib.request
import json
url = 'https://datos.cdmx.gob.mx/api/3/action/datastore_search?resource_id=ad360a0e-b42f-482c-af12-1fd72140032e&limit=1000'  
fileobj = urllib.request.urlopen(url)
data = fileobj.read()


dict_data= json.loads(data.decode('utf-8'))
with open('data.json', 'w') as json_file:
    json.dump(dict_data, json_file)
#print(json.dumps(dict_data, sort_keys=False, indent=4))