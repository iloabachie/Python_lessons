from selenium import webdriver
import os, dotenv  # py -m pip install python-dotenv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# https://selenium-python.readthedocs.io/installation.html

dotenv.load_dotenv(r'day48-selenium\.env')
token = os.getenv('EMAIL')
username = os.getenv('USERZNAME')

# print(00000, webdriver.__version__)
# print(1111, token, username)
# print(2222, os.environ.get('TOKEN'))
# print(3333, os.getenv('TEMP'))
# print(4444, os.environ.get('EMAIL'))

# chrome_driver_path = r"day48-selenium\ChromeDriver\chromedriver.exe"
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()

driver.get('https://www.google.com/')
print(555, driver.title)
element = driver.find_element(By.NAME, 'q')
element.send_keys(token)
print(element)
print(element.text)
time.sleep(5)
element.send_keys(Keys.RETURN)

# element.click()

time.sleep(7)

driver.close() # closes active tab
driver.quit() # closes the window


# print(dir(webdriver))
# print()
# print(dir(driver))
