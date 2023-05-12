from bs4 import BeautifulSoup
import requests
from csv import writer



url1 = "https://www.wheels97.com/car-brands"


page = requests.get(url1)

# print(page)
soup = BeautifulSoup(page.content,'html.parser')
# /print("SOUP!",soup)
lists = soup.find_all('h2', class_="c0146")
for list in lists:
    brands = list.text
    
    print(brands)