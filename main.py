from typing import Optional
from fastapi import  FastAPI
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
  title:str
  content:str
  published:bool = True
  rating:Optional[int] = None
  
my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}] 

#get methods
#if both the path are same and the methods are also same then the first get method is considered order matters.

@app.get("/")
async def root():
  return {"message":"Welcome to my api"}

@app.get("/posts")
def get_posts():
  return {"data":my_posts}

#post methods

@app.post("/posts")
def create_posts(post:Post):
  post_dict = post.model_dump()
  post_dict['id'] = randrange(0,1000000)
  my_posts.append(post_dict)
  return {"message":post_dict}


@app.get("/posts/{id}")
def get_post(id):
  print(id)
  return f"post_detail:{id}"