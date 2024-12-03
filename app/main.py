from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db.database import engine
from .db import models
from .routes import external, auth, crud, user

app = FastAPI()

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





@app.get("/")
def root():
    return {"message": "welcome to my project"}