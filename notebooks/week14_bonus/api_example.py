import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

city = "Bremen"
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Location:", data["location"]["name"], data["location"]["region"], data["location"]["country"])
    print("Temperature:", data["current"]["temp_c"], "°C")
else:
    print("Failed to fetch weather data")
