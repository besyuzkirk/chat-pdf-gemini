from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv() 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PDF Chat API is running!"}
