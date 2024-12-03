from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class WeatherBase(BaseModel):
    city: str
    temperature: float


class WeatherCreate(WeatherBase):
    pass


class WeatherResponse(WeatherBase):
    id: int

    class Config:
        orm_mode = True 



class UserBase(BaseModel):
    email: EmailStr  


class UserCreate(UserBase):

    password: str


class UserResponse(UserBase):

    id: int
    created_at: datetime

    class Config:
        orm_mode = True
