import requests

# https://home.openweathermap.org/api_keys

parameters = {
    'lon': -79.252357,
    'lat': 43.774578,
    'units': 'metric',
    'appid': '9f10b50c0febf1e66bc7131091374408',
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
weather = response.json()

print('hello', response.status_code, end='\n------------------------------------\n')

print(weather)


