from typing import Union

from fastapi import FastAPI

app = FastAPI()
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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users")
def moje_funkce():
    return {"users": uzivatele}


@app.get("/users/{id}")
def find_user(id: int):
    for user in uzivatele:
        if user["id"] == id:
            return {"user": user}
