from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class WeatherBase(BaseModel):
    city: str
    temperature: float
    created_at: datetime
    id: int

class WeatherCreate(BaseModel):
    city: str


class WeatherResponse(WeatherBase):
    id: int
    owner_id: int 

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
        from_attributes = True


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None
