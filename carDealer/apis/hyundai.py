import requests
import json
import pandas as pd
import numpy as np
import database
from concurrent.futures import ThreadPoolExecutor


json_path = '/home/shubham/UnicornTech/web_scrapping/carDealer/data/hyundai.json'
url = "https://api.hyundai.co.in/service/dealer/getModels?loc=IN&lan=en"
response = requests.get(url)
response = response.text
cars = json.loads(response)
model_ids = [car["id"] for car in cars]
# model_ids = [24, 39, 41, 19, 35, 45, 18, 37, 40, 42, 43]

# with open(json_path, 'r') as f:
#      data = json.load(f)
# print(data)
# to delete data from hyundai.json list
# data_cleaned = [{k:v for k,v in d.items() if k!='code' and k!='version'} for d in data]
# state_ids = [item["id"] for item in data]
state_ids =[2, 4, 5, 6, 7, 10, 11, 12, 14, 15, 16, 17, 19, 20, 25, 26, 28, 29, 31, 32, 34, 35, 36]
# https://api.hyundai.co.in/service/dealer/getAlcazarCities?stateId=10&dealerCategory=1&modelId=45&variantId=&loc=IN&lan=en
base_url = "https://api.hyundai.co.in/service/dealer/getAlcazarCities?dealerCategory=1"
city_ids = []
for state_id in state_ids:
    for model_id in model_ids:
        url1 = base_url + f"&stateId={state_id}&modelId={model_id}&variantId="
        city = requests.get(url1)
        city = city.text
        city = json.loads(city)
        city_id = {item['id'] for item in city}
        city_ids.append(city_id)

url = 'https://api.hyundai.co.in/service/dealer/getAlcazarDealers?dealerCategoryId=1&cityId={}&modelId={}&variantId='
data_list = []
def get_dealers(city_id, model_id):
    response = requests.get(url.format(city_id, model_id))
    all_data = response.json()
    data_list.append(all_data)

    return all_data

with ThreadPoolExecutor(max_workers=10) as executor:
    for city_id_set in city_ids:
        for model_id in model_ids:
            for city_id in city_id_set:
                future = executor.submit(get_dealers, city_id, model_id)
                all_data = future.result()
print(data_list)
