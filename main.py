from typing import Optional
from fastapi import FastAPI
from utils import queryText

app = FastAPI()

@app.get("/")
def index(q:str):
    result = queryText(q)
    return {"message" : result}
