import datetime
from app.config import API_KEY, BASE_URL
import requests

def fetch_weather(city: str):

    #Fetch the weather for a specific city.

    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    res = response.json()
    city_name = res["city"]["name"]
    temperature = res["list"][0]["main"]["temp"]

    timestamp = res["list"][0]["dt"]  # Get the timestamp from the first weather data point
    date = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    return {"city": city_name, "temperature": temperature, "date":date}




