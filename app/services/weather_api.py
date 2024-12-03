import httpx
from app.config import API_KEY, BASE_URL

import requests
from app.config import API_KEY, BASE_URL

def fetch_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    res = response.json()
    city_name = res["city"]["name"]
    temperature = res["list"][0]["main"]["temp"]
    return {"city": city_name, "temperature": temperature}




