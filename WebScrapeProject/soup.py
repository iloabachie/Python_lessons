from bs4 import BeautifulSoup as BS
import requests


url = 'https://www.salvagemarket.co.uk/Search?auction=&bucketDetails=&bucketId=&damageCategory=&distance=&editorPickSearch=0&fuelType=&latitude=0&longitude=0&make=&orderBy=1&pageNumber=0&pageSize=20&searchText=&seller=Hills%20Salvage%20%26%20Recycling%20Ltd&transmissionType='
# url = "https://www.google.com"
r = requests.get(url)
soup = BS(r.content, 'html.parser')
print(r)
print(soup)

#usage
item = soup.find('img', {'alt': "Avatar"})['src']
print(item)