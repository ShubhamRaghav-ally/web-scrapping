from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service(executable_path="/home/shubham/Downloads/chromedriver_linux64/chromedriver")


url ='https://www.zigwheels.com/newcars/Kia'

with webdriver.Chrome(service=service) as driver:
    with open('KIA_file.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        driver.get(url)
        driver.maximize_window()
        writer.writerow(['Title','Price'])

        elements = driver.find_elements(By.XPATH, "//a[@data-track-label='launched-model-name']")
        hrefs = [element.get_attribute('href') for element in elements]
        for href in hrefs:
            driver.get(href)
            price = driver.find_element(By.ID,"modelPrice")
            title= driver.find_element(By.TAG_NAME,"h1")
            # title1 = title.text
            print(price.text,title.text)
driver.quit()
table = driver.find_element_by_xpath("//table[@class='my-table']")

# Find all the rows in the table
rows = table.find_elements_by_tag_name("tr")

# Open a CSV file for writing
with open("table_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    # Loop over the rows and write the data to the CSV file
    for row in rows:
        # Find all the cells in the row
        cells = row.find_elements_by_tag_name("td")

        # Extract the text from each cell and write it to the CSV file
        row_data = [cell.text for cell in cells]
        writer.writerow(row_data)

