import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time


service = Service(executable_path="/home/shubham/Downloads/chromedriver_linux64/chromedriver")

url ='https://www.zigwheels.com/newcars/Kia'
PROXY = "11.456.448.110:8080"

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--proxy-server=%s' % PROXY)

with webdriver.Chrome(service=service) as driver:
    with open('my_file.csv', mode='w', newline='') as file:
        writer = csv.writer(file)

        # with webdriver.Chrome(service=service) as driver:
        driver.get(url)
        # time.sleep(20)
        writer.writerow(['Title','Price','Specs'])
        driver.maximize_window()
        # driver.get
        elements = driver.find_elements(By.XPATH, "//a[@data-track-label='launched-model-name']")
        hrefs = [element.get_attribute('href') for element in elements]
        for href in hrefs:
            driver.get(href)
            WebDriverWait(driver,10)
            title= driver.find_element(By.TAG_NAME,"h1")
            price = driver.find_element(By.ID,"modelPrice")
            table = driver.find_element(By.XPATH,"//table[@class='zw-bikeover-table ns-spec']")
            rows = table.find_elements(By.TAG_NAME,"tr")
            variant = driver.find_element(By.XPATH,'//a[@data-track-label="variant-tab"]')
            hover = ActionChains(driver).move_to_element(variant)
            WebDriverWait(driver=10,timeout=40)
            hover.perform() 
            # list_elements = driver.find_elements(By.XPATH,"//*[@id='varSrRes']")
            # list_elements= WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(By.XPATH,"//*[@id='varSrRes']"))
            list_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='varSrRes']/li")))
            # data_href = list_elements.get_attribute("data-href")
            # print(data_href)
            # driver.refresh()
            print("-------")
            print(list_elements)
            print("-------")

            print("---FOR LOOP START HERE----")

            for element in list_elements:
                print(element.text)
                print("---element----")
                print(element)

                list_elements = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='varSrRes']/li")))
                print(list_elements)
                href = element.get_attribute("data-href")
                print(href)
                
                # driver.get(href)
                # driver.back()
                # driver.refresh()
                

# driver.quit()
                # print("+++>>",title.text,list_elements.get_property('data-href'))
                       

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                # scroll_menu.select_by_visible_text("Option 1")//li[@class="var-lst a"]
                # print(scroll_menu.select_by_visible_text)

                # info=[]
                # for row in rows:
                #             cells = row.find_elements(By.TAG_NAME,"td")
                #             row_data = [cell.text for cell in cells]
                #             dictionary = {'row_data': row_data}
                #             info.append(dictionary)
                #             # print(info)
                # # print(info)
                # data=[title.text,price.text,info]      
                # writer.writerow(data)


