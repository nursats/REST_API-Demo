import httpx
from app.config import API_KEY, BASE_URL

async def fetch_weather(city: str):
    params = {"q": city, "appid": API_KEY}
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise error for bad responses
        res = response.json()
        return res['city']
