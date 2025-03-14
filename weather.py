from dotenv import load_dotenv
import os
import requests

# load environment variables from .env file
load_dotenv()

# get the API key from the environment variable
api_key = os.getenv('WEATHER_API_KEY')
if not api_key:
    raise ValueError('API key is not set')

api_url = os.getenv('WEATHER_API_URL')
if not api_url:
    raise ValueError('API URL is not set')

city = input("Enter city name: ")

request_url = f"{api_url}?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(request_url)
    # check if the request was successful
    response.raise_for_status()  
    data = response.json()
    temp = data["main"]["temp"]
    print(f"Current temperature in {city}: {temp}°C")
except requests.RequestException as e:
    print(f"Error fetching weather data: {e}")