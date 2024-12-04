from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func

from app.db import models
from app.schemas import schemas
from app.db.database import get_db
from app.services.weather_api import fetch_weather
from .. import oauth2


router = APIRouter(
    prefix="/weather",
    tags=['Weather']
)

@router.get("/", response_model=List[schemas.WeatherResponse], summary="get all weather data")
def get_weather_data(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    data = db.query(models.WeatherData).filter(models.WeatherData.owner_id == current_user.id).all()
    return data


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.WeatherBase, summary="Create weather data")
def create_weather(weather_request: schemas.WeatherCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    """
    **Request Body Example**:

    json
    {
      "city": "Nur-Sultan",
    }
    

    **Response Example**:

    json
    {
      "id": 1,
      "city": "Nur-Sultan",
      "temperature": -10.5,
      "owner_id": 1,
      "created_at": "2024-12-03T12:00:00Z"
    }
    """

    city = weather_request.city

    try:
        weather_data = fetch_weather(city)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to fetch weather data for city '{city}'. Error: {str(e)}"
        )

    new_weather = models.WeatherData(
        city=weather_data["city"],
        temperature=weather_data["temperature"],
        owner_id=current_user.id  
    )
    db.add(new_weather)
    db.commit()
    db.refresh(new_weather)

    return new_weather
    

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete weather data")
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):


    weather_query = db.query(models.WeatherData).filter(models.WeatherData.id == id)

    weather = weather_query.first()

    if weather == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"weather with id: {id} does not exist")

    if weather.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    weather_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.WeatherBase, summary="Update city in weather data")
def update_post(id: int, updated_post: schemas.WeatherCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):


    weather_query = db.query(models.WeatherData).filter(models.WeatherData.id == id)

    weather = weather_query.first()

    if weather == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    


    if weather.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    weather_query.update(updated_post.model_dump(), synchronize_session=False)

    db.commit()

    return weather_query.first()


@router.get("/weather-info/{city}", response_model=schemas.WeatherResponse)
def get_weather_info(city: str, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    weather = db.query(models.WeatherData).filter(func.lower(models.WeatherData.city) == city.lower()).first()

    if weather:
        return weather
    try:
        weather_data = fetch_weather(city)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to fetch weather data for city '{city}'. Error: {str(e)}"
        )

    new_weather = models.WeatherData(
        city=weather_data["city"],
        temperature=weather_data["temperature"],
        owner_id=current_user.id
    )
    db.add(new_weather)
    db.commit()
    db.refresh(new_weather)

    return new_weather
