import requests
import dotenv # py -m pip install python-dotenv
import os
import datetime

today = datetime.datetime.now()

year = today.year
month = today.month
day = today.day

print(year, month, day)
print(today.strftime('%Y---%M//%d'))

dotenv.load_dotenv('./day37-habit/.env')

token = os.getenv('TOKEN')
username = os.getenv('USERZNAME')

print(token, username)

create_endpoint = "https://pixe.la/v1/users"

parameters = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'    
}

# response = requests.post(url=create_endpoint, json=parameters)
# print(response.json(), '*****************')
# print(response.text)

graph_endpoint = f'{create_endpoint}/{username}/graphs'

graph_id = 'graph1'

graph_config = {
    'id': graph_id,
    'name': 'gym time',
    'unit': 'minutes',
    'type': 'float',
    'color': 'shibafu'
}

header = {
    'X-USER-TOKEN': token
}

# response2 = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response2.text)


add_val_endpoint = f'{create_endpoint}/{username}/graphs/{graph_id}'

post_config = {
    'name': 'gym time',
    'date': f'{year}{month}{day}',
    'quantity': '65.6',
    'optionalData': 'This is optional data'
}

response3 = requests.put(url=add_val_endpoint, json=post_config, headers=header)
print(response3.text)
print(f'{year}{month}{day}')