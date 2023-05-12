import requests
import os
import json
import re

import pandas as pd
import database
url = "https://www.jeep-india.com/content/dam/cross-regional/apac/jeep/en_in/ebook/jeep-dealers.js"
variable = requests.get(url)
response = variable.text
response = json.loads(response)

df2 = pd.json_normalize(response['sales'])
df1 = pd.json_normalize(response['services'])
df = pd.concat([df2, df1], ignore_index=True)
make_id = 26
new_columns =["v_type_id","v_make_id","category"]
new_values = [1,make_id,"car"]
toyota_scheme = {"division":"oem","dealerName":"company_name" ,"dealerAddress1":"address","demail" : "email","website":"website","phoneNumber":"phone" ,"dealerShowroomLatitude":  "latitude","dealerShowroomLongitude":  "longitude","dealerCity":"city_name","dealerState":"state_name","department":"outlet_type","dealerZipCode":"pincode" }
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

print(each_row.iloc[67])

database.insert_customer(each_row)