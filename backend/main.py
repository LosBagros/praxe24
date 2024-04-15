from typing import Union, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware
import json
import os

origins = ["*"]


class LinkIcon(BaseModel):
    url: HttpUrl
    icon: str


class User(BaseModel):
    id: int
    username: str
    pfp_url: HttpUrl
    links: Optional[List[LinkIcon]] = None


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=origins)


uzivatele = json.load(open("users.json"))


if os.path.exists("user_seed.json"):
    uzivatele = json.load(open("user_seed.json"))


@ app.get("/users")
def get_all_users():
    return {"users": uzivatele}


@ app.get("/users/{id}", response_model=User)
def find_user(id: int):
    for user in uzivatele:
        if user["id"] == id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
