import json
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
chrome_options = Options()
with webdriver.Chrome(service=service) as driver:
    with open('/home/shubham/UnicornTech/web_scrapping/car_webScrapping/data.json', 'r') as infile:
        data = json.load(infile)
    hrefs = []
    for car in data:
        for variant in car['Variants']:
            hrefs.append(variant['href'])
    for href in hrefs:
        driver.get(href)
        # print(href)
        # featureSpecs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((driver.find_element(By.XPATH,'//div[@class="spec-mar-first rvmp_specs-accordion"]'))))
        featureSpecs = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="spec-mar-first rvmp_specs-accordion"]')))

        print(featureSpecs.text)
        for x in featureSpecs:
            title = driver.find_element(By.XPATH,'//*[@onclick="readMoreText();"]').text
            print(title)
driver.quit()
    



