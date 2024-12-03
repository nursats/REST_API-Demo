from fastapi import APIRouter
from app.services.weather_api import fetch_weather

router = APIRouter()

@router.get("/test")
async def test_external_api(city: str = "London"):
    return await fetch_weather(city)