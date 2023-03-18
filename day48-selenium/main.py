from selenium import webdriver
import os, dotenv  # py -m pip install python-dotenv

dotenv.load_dotenv(r'day48-selenium\.env')
token = os.getenv('EMAIL')
username = os.getenv('USERZNAME')


print(1111, token, username)
print(2222, os.environ.get('TOKEN'))
print(3333, os.getenv('TEMP'))

chrome_driver_path = r"D:\Documents\Python lessons\ChromeDriver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://toronto.citynews.ca/2022/11/07/the-citynews-680-weather-guarantee/')
driver.find_element_by_xpath('//*[@id="main"]/div/div/article[2]/div/div/a')

driver.close() # closes active tab
driver.quit() # closes the window


