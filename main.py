from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]


class Uzivatel(BaseModel):
    id: int
    name: str
    img_url: HttpUrl
    links: List[HttpUrl]


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=origins)

uzivatele = [
    {
        "id": 1,
        "name": "Tom",
        "img_url": "https://placehold.co/200",
        "links": ["https://placehold.co/200",
                  "https://placehold.co/200",
                  "https://placehold.co/200"]

    },
    {
        "id": 2,
        "name": "Jakub",
        "img_url": "https://placehold.co/200",
        "links": ["https://placehold.co/200",
                  "https://placehold.co/200",
                  "https://placehold.co/200"]

    },
    {
        "id": 3,
        "name": "Pepa",
        "img_url": "https://placehold.co/200",
        "links": ["https://placehold.co/200",
                  "https://placehold.co/200",
                  "https://placehold.co/200"]

    }
]


@ app.get("/")
def read_root():
    return {"Hello": "World"}


@ app.get("/users")
def moje_funkce():
    return {"users": uzivatele}


@ app.get("/users/{id}")
def find_user(id: int):
    for user in uzivatele:
        if user["id"] == id:
            return {"user": user}
