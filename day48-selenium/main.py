from selenium import webdriver
import os, dotenv  # py -m pip install python-dotenv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

dotenv.load_dotenv(r'day48-selenium\.env')
token = os.getenv('EMAIL')
username = os.getenv('USERZNAME')


chrome_driver_path = r"day48-selenium\ChromeDriver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://toronto.citynews.ca/contests/')

time.sleep(5)
element = driver.find_element(By.LINK_TEXT, 'The CityNews 680 Weather Guarantee')
# print(element)
print(element.text)

element.click()

time.sleep(100000)

driver.close() # closes active tab
driver.quit() # closes the window


print(os.environ.get("EMAIL"))