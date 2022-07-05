from fastapi import FastAPI
from typing import Union, Dict, List
from pydantic import BaseModel

app = FastAPI()


class Timeslot(BaseModel):
    searchTerm: str


class Delivery(BaseModel):
    pass


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/timeslots/")
async def timeslots(timeslot: Timeslot):
    return timeslot


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
