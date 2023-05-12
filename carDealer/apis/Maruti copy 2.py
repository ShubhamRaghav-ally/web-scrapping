import pandas as pd
import json
import itertools
import database
data = ['{"data":[{"website":"https://mg-brothers.in.kia","dealerName":"MG Brothers, NH44, Bangalore Hwy","address3":"Anantapur 515002","lng":"77.58245","address2":" Kakkalapalli Vill,","cityCode":"S99","address1":"1-374, NH44, Bangalore Hwy,","phone2":"999999999","phone1":"8333099186","cityName":"Anantpur","stateName":"Andhra Pradesh","sortId":"1","dealerType":"Sales","stateCode":"AP","id":"AP301","email":"gmsalesatp@mgbrotherskia.in","lat":"14.64879"},{"website":"https://mg-brothers.in.kia","dealerName":"MG Brothers, NH44, Bangalore Hwy","address3":"Anantapur","lng":"77.58245","address2":"1-374, NH44, Bangalore Hwy, Kakkalapalli Vill,","cityCode":"S99","phone2":"999999999","phone1":"9494436198","cityName":"Anantpur","stateName":"Andhra Pradesh","sortId":"3","dealerType":"Service","stateCode":"AP","id":"AP301","email":"serviceatp@mgbrotherskia.in","lat":"14.64879"}],"resultCode":"0000","message":""}', '{"data":[{"website":"https://simha-kia.in.kia","dealerName":"Simha Kia, Undi Highway","address3":"Bhimavaram – 534202","lng":"81.496515","address2":"Near Agriculture Check post, ","cityCode":"S61","address1":"SY No:140/2B, Pedamiram Undi Road, ","phone2":"999999999","phone1":"7331122044","cityName":"Bhimavaram","stateName":"Andhra Pradesh","sortId":"1","dealerType":"Sales","stateCode":"AP","id":"AP306","email":"salesmanager.bvrm@simha-kia.in","lat":"16.562355"},{"website":"https://simha-kia.in.kia","dealerName":"Simha Kia, Undi Highway","address3":"Bhimavaram – 534202","lng":"81.496515","address2":"Near Agriculture Check post, ","cityCode":"S61","address1":"SY No:140/2B, Pedamiram Undi Road, ","phone2":"999999999","phone1":"9573441726","cityName":"Bhimavaram","stateName":"Andhra Pradesh","sortId":"3","dealerType":"Service","stateCode":"AP","id":"AP306","email":"Servicemanager.bvrm@simha-kia.in; ","lat":"16.562355"}],"resultCode":"0000","message":""}']
data_list = []
df = pd.DataFrame(data)
for index, row in df.iterrows():
    data = json.loads(row[0])['data']
    data_list.append(data)
print(data_list)

flattened_list = []
for sublist in data_list:
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
print(df2)   
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
    
print(each_row)
database.insert_customer(each_row)