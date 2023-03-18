import requests
from datetime import datetime
import time

place = 'Scarborough'

MY_LAT = 43.774578 if place == 'Scarborough' else 52.29091929389333    # Your latitude
MY_LONG = -79.252357 if place == 'Scarborough' else 21.019662397578625 # Your longitude

def is_visible():
    global iss_latitude, iss_longitude
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5) and (time_now <= sunrise or time_now >= sunset):
        return True
    else:
        return False


while True:
    with open("day33-iss_tracker/log.txt", mode='a') as log:        
        if is_visible():
            print('******Look up for the ISS', datetime.now(), f'at coordinate {iss_longitude}, {iss_latitude}')
            log.write(f'******Look up for the ISS {datetime.now()} at coordinate {iss_longitude}, {iss_latitude}')           
        else:
            print('Not visible at this time:', datetime.now(), f'at coordinate {iss_longitude}, {iss_latitude}')
            log.write(f'Not visible at this time: {datetime.now()} at coordinate {iss_longitude}, {iss_latitude}')
    time.sleep(6)
