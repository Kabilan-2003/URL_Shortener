from fastapi import FastAPI
from .routes import route
from .database import Base, engine
from .models import URL


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(route)

@app.get("/")
async def root():
    return {"message": "Hello World"}