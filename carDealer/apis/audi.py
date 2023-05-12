import requests
import json
import pandas as pd
import numpy as np
import database
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
url = "https://secure.zala.net/api/staff/location/list?field=updatedOn&sort=asc"
headers = {
    "Authorization":"Bearer 1dba5121afaad1b703fa635b1e933c9d",
    "Connection": "keep-alive",
}
response = requests.get(url,headers=headers)
response = response.text
response = json.loads(response)
df = pd.json_normalize(response['data']['items'])
df = df.replace("\t","")
# df.to_csv('my_data.csv', index=False)
df = df.drop('googleMap', axis=1)

make_id = 11
new_columns =["v_type_id","v_make_id","category","oem"]
new_values = [1,make_id,"car","Audi"]
toyota_scheme = {"merchantName":"company_name" ,"address":"address","emailIds" : "email","clickUrl":"website","phoneNumber1":"phone" ,"lat":  "latitude","lon":  "longitude","categoryNames":"outlet_type" }
toyota_db_fields = [value for value in toyota_scheme.values()]
df.rename(columns=toyota_scheme,inplace=True)
columns_list = df.columns.tolist()
each_row = df.loc[:, toyota_db_fields]
new_data = dict(zip(new_columns, new_values))
for col, val in new_data.items():
    each_row[col] = val
each_row['latitude'] = each_row['latitude'].str.replace('"', '').str.replace("'", "")
each_row['longitude'] = each_row['longitude'].str.replace('"', '').str.replace("'", "")
each_row['address'] = each_row['longitude'].str.replace("'", "")
# each_row['outlet_type'] = each_row['outlet_type'].astype(str)

each_row['outlet_type'] = each_row['outlet_type'].astype(str).str.strip('[]').str.replace("'", "")
# INSERT INTO 91wheels_scrap_dealers SET `company_name`='None', `address`='72.8599112', `email`='None', `website`='https://secure.zala.net/staff/location/view/75', `phone`='None', `latitude`='19.1129657', `longitude`='72.8599112', `outlet_type`=''All Categories'', `v_type_id`='1', `v_make_id`='11', `category`='car', `oem`='Audi'

print(each_row['outlet_type'])

database.insert_customer(each_row)
# https://api.hyundai.co.in/service/dealer/getAlcazarCities?stateId=10&dealerCategory=1&modelId=45&variantId=
# urls = [f"https://api.hyundai.co.in/service/dealer/getAlcazarCities?stateId={state_id}&dealerCategory=1&modelId={model_id}&variantId=" for state_id in state_ids for model_id in model_ids]
# print(urls)
# def get_response(url):
#     response = requests.get(url)
#     return response.json()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     responses = list(executor.map(get_response, urls))
# print(responses)
