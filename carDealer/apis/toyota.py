import requests
import ast
import json
import os
import csv
import xmltodict
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import database
import pandas as pd
import numpy as np

url = "https://staging.webapi.toyotabharat.com/1.0/api/salescities"

response = requests.post(url)
dealer_oem = "Toyota"
stateAndCity = response.text
response_dict = xmltodict.parse(stateAndCity)

response_json = json.dumps(response_dict,indent=4)
json_data = json.loads(response_json)
cities = json_data["Cities"]["City"]
city_ids =[]
list = {}
urls =[]
data_list = []
# to find city ids and getting the urls accordingly
for City in cities:
    city_id = City["Id"]
    city_name = City["Name"]
    list[city_id] = city_name
    city_ids.append(city_id)
    url =f"https://staging.webapi.toyotabharat.com/1.0/api/businesscities/{city_id}/websalesdealers"
    urls.append(url)
for url in urls:   
    variable = requests.post(url)
    xml_response = variable.text
    root = ET.fromstring(xml_response)
    headers = []
    for child in root:
        data = {}
        for subchild in child:
            tag = subchild.tag
            value = subchild.text.strip() if subchild.text else ''
            # check if there are multiple data under one tag
            if subchild.findall('.//*'):
                value_list = []
                for subsubchild in subchild:
                    if subsubchild is None:
                        value_list.append(subsubchild.text.strip())
                value = ';'.join(value_list)

            if tag not in headers:
                headers.append(tag)
            data[tag] = value
        data_list.append(data)
merged_key = 'Address'
keys_to_merge = ['Address1', 'Address2', 'Address3','Address4']

for d in data_list:
    values_to_merge = []
    city_id = d.get("CityId")
    for key in keys_to_merge:
        if key in d:
            values_to_merge.append(d[key])
            del d[key]
    if values_to_merge:
        d[merged_key] = ', '.join(values_to_merge).replace(',,',',')
    if city_id in list:
        d["City"] = list[city_id]
            
df = pd.DataFrame(data_list)
dealer_oem = "Toyota"
dealer_id = 4
outlet_type ="showroom"
new_columns =["oem","v_type_id","v_make_id","category","outlet_type"]
new_values = [dealer_oem,1,dealer_id,"car",outlet_type]
toyota_scheme = {"Name":"company_name" ,"Address":"address","Pincode" : "pincode","URL":"website","Phone":"phone" ,"Latitude":  "latitude",
          "Longitude":  "longitude","City":"city_name" }
df['Address'] = df['Address'].str.replace("'", "")
toyota_db_fields = [value for value in toyota_scheme.values()]
df.rename(columns=toyota_scheme,inplace=True)
each_row = df.loc[:, toyota_db_fields]
each_row['name'] = each_row['company_name']
new_data = dict(zip(new_columns, new_values))

# Add the new columns to the dataframe and set their values to the new values
for col, val in new_data.items():
    each_row[col] = val
    
# print(each_row)

database.insert_customer(each_row)