from fastapi import APIRouter
from app.services.weather_api import fetch_weather

router = APIRouter()

@router.get("/test")
def test_external_api(city: str = "Astana"):
    return fetch_weather(city)


@router.get("/test")
def test_external_api(city: str = "Astana"):
    return fetch_weather(city)