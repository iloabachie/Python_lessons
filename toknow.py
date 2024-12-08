# https://www.youtube.com/watch?v=yf2xznF30-s
# tdqm, rich, pathlib, pydantic, ruff

from tqdm import tqdm
from time import sleep


for i in tqdm(range(10000)):
    x = 10 + i
    # if not i % 100:
    #     print(i)
        
from rich import print

print(f"'hello', 'man'")


import random

# Generate weather data
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
weather_types = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy", "Stormy"]

# Function to generate random weather data for a day
def generate_daily_weather():
    return {
        "temperature": round(random.uniform(-10, 40), 1),  # Temperature in Celsius
        "humidity": random.randint(10, 100),              # Humidity in percentage
        "wind_speed": round(random.uniform(0, 20), 1),    # Wind speed in km/h
        "weather": random.choice(weather_types)           # Weather description
    }

# Create a large dictionary
weather_data = {
    city: {
        f"2024-12-{day:02d}": generate_daily_weather()
        for day in range(1, 32)  # Data for each day in December
    }
    for city in cities
}

# Example: Print the weather data for a specific city
print(weather_data["New York"])
