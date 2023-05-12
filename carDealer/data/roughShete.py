# city_ids = [{913, 1067, 1419, 1442}, {1419}]
# model_ids = [24, 39, 41, 19, 35, 45, 18, 37, 40, 42, 43]

# url_template = "https://api.hyundai.co.in/service/dealer/getAlcazarDealers?dealerCategoryId=1&cityId={city_ids}&modelId={model_id}&variantId="

# for model_id in model_ids:
#     city_id_str = ','.join(str(city_id) for city_id in set.union(*city_ids))
#     url = url_template.format(city_ids=city_id_str, model_id=model_id)
#     print(url)
import requests
from concurrent.futures import ThreadPoolExecutor
city_ids = [{913, 1067, 1419, 1442}, {1419}]

# Define the URL and model IDs
url = 'https://api.hyundai.co.in/service/dealer/getAlcazarDealers?dealerCategoryId=1&cityId={}&modelId={}&variantId='
model_ids = [24, 39, 41, 19, 35, 45, 18, 37, 40, 42, 43]
data_list = []

# Define a function to make the API call
def get_dealers(city_id, model_id):
    response = requests.get(url.format(city_id, model_id))
    data = response.json()
    return data

# Create a thread pool with 10 workers
with ThreadPoolExecutor(max_workers=10) as executor:
    # Iterate over the city IDs and model IDs, and submit each combination to the thread pool
    for city_id_set in city_ids:
        for model_id in model_ids:
            for city_id in city_id_set:
                future = executor.submit(get_dealers, city_id, model_id)
                # Handle the response here, e.g. store it in a list or write to a file
                data = future.result()
                data_list.append(data)
print(data_list)