
from fastapi import FastAPI
from passlib.context import CryptContext

from . import models
from .database import engine
from .routers import auth, posts, users,vote

pwd_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")






models.Base.metadata.create_all(bind=engine)



app = FastAPI()
  
  
  
  

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
  return {"message":"Welcome to my api"}


  
  
