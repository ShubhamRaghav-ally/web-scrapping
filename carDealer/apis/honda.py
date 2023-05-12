import requests
import json
import database
import pandas as pd
# pd.set_option('display.max_columns', None)


json_path = '/home/shubham/UnicornTech/web_scrapping/carDealer/data/honda.json'
with open(json_path, 'r') as f:
    data_list = json.load(f)
data_list = data_list["data"]
st_ids = [d["St_ID_pk"] for d in data_list]
urls = []
responses = []
for state in st_ids:
    url =f"https://www.hondacarindia.com/api/getAllDealerViaTypes?cityId={state}&radius=200"
    urls.append(url)
for url in urls:
    response = requests.get(url)
    response = response.text
    responses.append(response)
data = [json.loads(response)["data"] for json_str in responses]

df = pd.DataFrame(responses)
list  = []
for index, row in df.iterrows():
    responses = json.loads(row[0])['data']
    list.append(responses)

df1 = pd.DataFrame([d for l in data for d in l])
make_id = 3
new_columns =["v_type_id","v_make_id","category","oem"]
new_values = [1,make_id,"car","Honda"]
toyota_scheme = {"DD_companyName":"company_name","DD_address":"address","DD_email" : "email","DealerWebsite":"website","DD_telephone":"phone","latitude":"latitude","longitude":"longitude","outlettype":"outlet_type","DD_pincode":"pincode" }

toyota_db_fields = [value for value in toyota_scheme.values()]
df1.rename(columns=toyota_scheme,inplace=True)
columns_list = df1.columns.tolist()
each_row = df1.loc[:, toyota_db_fields]
new_data = dict(zip(new_columns, new_values))

for col, val in new_data.items():
    each_row[col] = val
# each_row['latitude'] = each_row['latitude'].str.replace('"', '').str.replace("'", "")
# each_row['longitude'] = each_row['longitude'].str.replace('"', '').str.replace("'", "")
# each_row['address'] = each_row['longitude'].str.replace("'", "")


database.insert_customer(each_row)
