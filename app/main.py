

from fastapi import  FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from passlib.context import CryptContext
import time
from . import models
from .database import  engine
from .routers import posts,users,auth
 

pwd_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")


models.Base.metadata.create_all(bind=engine)



app = FastAPI()


  
while True:  
  try:
    conn = psycopg2.connect(host='localhost',
                            database='fastapi',
                            user='postgres',
                            password='Step',
                            cursor_factory=RealDictCursor
                            )
    cursor = conn.cursor()
    print("Database connection was successful!")
    break
  except Exception as error:
    print("Connecting to database failed")
    print("The error was",error)
    time.sleep(2)
  
  
  
  

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)

@app.get("/")
async def root():
  return {"message":"Welcome to my api"}


  
  
