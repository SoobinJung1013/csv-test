from fastapi import FastAPI
from app import insert_data

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the API!"}


@app.post("/insert")
def insert():

    return insert_data()
