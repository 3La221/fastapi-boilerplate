from fastapi import FastAPI
from app.db.session import engine
from app.db import base 

app = FastAPI(title="API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to the API"}
