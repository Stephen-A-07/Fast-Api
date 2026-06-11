
from fastapi import FastAPI
from passlib.context import CryptContext
from .routers import auth, posts, users,vote
from fastapi.middleware.cors import CORSMiddleware


pwd_context = CryptContext(schemes=["bcrypt"],deprecated= "auto")

app = FastAPI()

origins = [
"*"
]


  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 
  
  

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
  return {"message":"Welcome to my api"}


  
  
