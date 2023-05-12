import requests
import os
import json
import pandas as pd
import database
# from data import KIA
json_path = '/home/shubham/UnicornTech/web_scrapping/carDealer/data/KIA.json'
with open(json_path, 'r') as f:
    data = json.load(f)

data_list = []
urls=[]
responses = []
for element in data:
    state_name = element['val1']['value']
    state_code = element['val1']['key']
    
    for city in element['val2']:
        city_name = city['value']
        city_code = city['key']
        
        data_list.append({'city_name': city_name, 'city_code': city_code, 'state_name': state_name, 'state_code': state_code})
for item in data_list:
    url = "https://www.kia.com/api/kia2_in/findAdealer.getDealerList.do?city={}&state={}".format(item['city_code'], item['state_code'])
    urls.append(url)

for url in urls:   
    variable = requests.post(url)
    xml = variable.text
    responses.append(xml)
list = []
df = pd.DataFrame(responses)
for index, row in df.iterrows():
    responses = json.loads(row[0])['data']
    list.append(responses)
flattened_list = []
for sublist in list:
    flattened_list.extend(sublist)
merged_key = 'Address'
keys_to_merge = ['address1', 'address2', 'address3','address4']
for d in flattened_list:
    values_to_merge = []
    for key in keys_to_merge:
        if key in d:
            values_to_merge.append(d[key])
            del d[key]
    if values_to_merge:
        d[merged_key] = ', '.join(values_to_merge).replace(',,',',')
df2 = pd.DataFrame(flattened_list)
dealer_oem = "kia"
make_id = 27
new_columns =["oem","v_type_id","v_make_id","category","outlet_type"]
new_values = [dealer_oem,1,make_id,"car"]
toyota_scheme = {"dealerName":"company_name" ,"Address":"address","email" : "email","website":"website","phone1":"phone" ,"lat":  "latitude",
          "lng":  "longitude","cityName":"city_name","stateName":"state_name","dealerType":"outlet_type" }
df2['Address'] = df2['Address'].str.replace("'", "")
toyota_db_fields = [value for value in toyota_scheme.values()]
df2.rename(columns=toyota_scheme,inplace=True)
each_row = df2.loc[:, toyota_db_fields]
each_row['name'] = each_row['company_name']
new_data = dict(zip(new_columns, new_values))

for col, val in new_data.items():
    each_row[col] = val
    
database.insert_customer(each_row)