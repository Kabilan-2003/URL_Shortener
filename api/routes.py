from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, get_db
from .keygen import generate_key
import validators

route = APIRouter()

@route.post("/urls/", response_model=schemas.URL)
async def create_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    if not validators.url(url.original_url):
        raise HTTPException(status_code=400, detail="Invalid URL")
    key = generate_key(db)
    db_url = models.URL(original_url=url.original_url, short_url=key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

@route.get("/{short_url}", response_model=schemas.URL)
async def read_url(short_url: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_url == short_url).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.original_url)