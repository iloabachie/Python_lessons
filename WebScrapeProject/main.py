from selenium import webdriver
import os, dotenv  # py -m pip install python-dotenv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# https://selenium-python.readthedocs.io/installation.html

dotenv.load_dotenv(r'WebScrapeProject\.env')

driver = webdriver.Chrome()

SCRAPE_URL = "https://www.salvagemarket.co.uk/Search?auction=&bucketDetails=&bucketId=&damageCategory=&distance=&editorPickSearch=0&fuelType=&latitude=0&longitude=0&make=&orderBy=1&pageNumber=0&pageSize=20&searchText=&seller=&transmissionType="


driver.get(SCRAPE_URL)
print(driver.title)

elements = driver.find_elements(By.CLASS_NAME, 'jss83')
print('jss1014 >>', len(elements))

for e in elements:
    print(e.text)
print()

elements = driver.find_elements(By.CLASS_NAME, 'MuiTypography-root')
print('MuiTypography-root >>', len(elements))

for e in elements:
    print(e.text)
print()

elements = driver.find_elements(By.CLASS_NAME, 'MuiTypography-h6')
print('LEN MuiTypography-h6 >>', len(elements))

for e in elements:
    print(e.text)
print()

#element.send_keys(token)
#print(element)
#print(element.text)


#element.send_keys(Keys.RETURN)

# element.click()

time.sleep(7)

driver.close() # closes active tab
driver.quit() # closes the window