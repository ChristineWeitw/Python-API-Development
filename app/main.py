from multiprocessing import synchronize
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
# from pydantic import BaseModel, EmailStr
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .database import engine, get_db
from .routers import post, user


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='Dodosocute!', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfull!")
        break
    except Exception as error:
        print("Connecting to database fail.")
        print("error: ", error)
        time.sleep(2)

# my_posts = [{"title": "Harry Potter", "content": "Must read in childhood.", "id": 1},
#             {"title": " Fav food", "content": "stinky tofu", "id": 2}]

# def find_post(id):
#     for p in my_posts:
#         if p["id"]==id:
#             return p
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id']==id:
#             return i

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to my fastAPI!"}