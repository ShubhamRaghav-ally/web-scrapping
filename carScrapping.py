from bs4 import BeautifulSoup
import requests
from csv import writer


url1 = "https://www.zigwheels.com/"

url = "https://www.zigwheels.com/newcars/Kia#leadform"
page = requests.get(url)
page1 = requests.get(url1)

print(page)
print(page1)

# soup = BeautifulSoup(page.content,'html.parser')
# lists = soup.find_all('div', class_="p-15 pt-10 mke-ryt rel")

# with open('Mercs.csv','w',encoding='utf8', newline = '') as f:
#     thewriter = writer(f)
#     header = ['Title','Engine','Price']
#     thewriter.writerow(header)
#     for list in lists:
#         title = list.find('h3').text
#         engine = list.find('div',class_='clr-pry fnt-12 pb-10 h-height lh-18 of-hid').text
#         price = list.find('div',class_='clr-bl').text.replace("Check On-road Price","")
#         info=[title,engine,price]
#         thewriter.writerow(info)
