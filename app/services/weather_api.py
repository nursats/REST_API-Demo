import httpx
from app.config import API_KEY, BASE_URL

async def fetch_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        res = response.json()
        
        city_name = res["city"]["name"]
        temperature = res["list"][0]["main"]["temp"]

        return {
            "city": city_name,
            "temperature": temperature
        }
    
