from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.database import engine
from .db import models
from .routes import external, auth, crud, user

app = FastAPI(
    title="Weather API",
    description="An API for managing weather data, with JWT authentication and external API integration.",
    version="1.0.0",
    contact={
        "name": "Nursat",
        "email": "nursat.seitov12@gmail.com"
    }
)

origins = ["*"]

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"],     
    allow_headers=["*"],    
)

app.include_router(external.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(crud.router)






@app.get("/")
def root():
    return {
        "message": "welcome to my project",
        "description": "This is a demo REST API project",
        "contact": "nursat.seitov12@gmail.com"
        }