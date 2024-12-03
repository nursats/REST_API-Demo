from fastapi import APIRouter, HTTPException, Depends, Response, status
from sqlalchemy.orm import Session
from typing import List, Optional
from sqlalchemy import func

from app.db import models
from app.schemas import schemas
from app.db.database import get_db

