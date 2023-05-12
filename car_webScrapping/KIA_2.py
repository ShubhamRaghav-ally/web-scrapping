from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
# Set up the Selenium driver with the Stealth module
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32")

# Navigate to the CarDekho website and search for car dealers
url = "https://www.cardekho.com/cardealers"
driver.get(url)
data = {"options": [], "states": []}

dropdown_menu_brand = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "oemName")))
action = ActionChains(driver)
action.move_to_element(dropdown_menu_brand).click().perform()
options_containers = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='gs_ta_results width100   ']")))
options = options_containers.find_elements(By.XPATH,"//*[@id='topBanner']/div[2]/div/div/div/div/ul/li[1]/div/div/div/ul/li")
for option in options:
    if option.is_enabled():
        data["options"].append(option.text)

dropdown_menu_state =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "cityDropDown1")))
action.move_to_element(dropdown_menu_state).click().perform()
options_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='gs_ta_results width100   ']")))
states = options_container.find_elements(By.XPATH,"//*[@id='topBanner']/div[2]/div/div/div/div/ul/li[2]/div/div/div/ul/li")


for state in states:
        if state.is_enabled():
                data["states"].append(state.text)
driver.quit()

json_data = json.dumps(data)
print(json_data)
# for option in options:
#     print(option.text)
driver.quit()