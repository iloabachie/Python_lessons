import requests
import json
import os
import dotenv
import ConsolePrint

dotenv.load_dotenv('weather/.env')

# https://home.openweathermap.org/api_keys

url='https://api.openweathermap.org/data/2.5/forecast'

parameters = {
    'lon': -79.252357,
    'lat': 43.774578,
    'units': 'metric',
    'appid': os.getenv('WEATHER_API')
}

response = requests.get(url=url, params=parameters)
try:
    response.raise_for_status()
except Exception as e:
    print('\033[31mError', f'{e=}\033[0m')
finally:
    weather = response.json()    

print(f'{response.status_code=}')

ConsolePrint.startConsoleSave('weather/summitsx')
print(json.dumps(weather, indent=3))
ConsolePrint.endConsoleSave(prompt=False)
if response.status_code is not 200:
    print(json.dumps(weather, indent=3)) 