from typing import Optional
from fastapi import  FastAPI, HTTPException, Response,status
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
  title:str
  content:str
  published:bool = True
  rating:Optional[int] = None
  
my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}] 

def find_post(id):
  for p in my_posts:
    if p['id'] == id:
      return p
    
def find_by_id(id):
  for i,p in enumerate(my_posts):
    if p['id'] == id:
      return i


#if both the path are same and the methods are also same then the first get method is considered order matters.

@app.get("/")
async def root():
  return {"message":"Welcome to my api"}

@app.get("/posts")
def get_posts():
  return {"data":my_posts}

#post methods

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
  post_dict = post.model_dump()
  post_dict['id'] = randrange(0,1000000)
  my_posts.append(post_dict)
  return {"message":post_dict}


@app.get("/posts/{id}")
def get_post(id:int):
  post = find_post(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
  return {"post_detail":post}

@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
  index_post = find_by_id(id)
  if index_post is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
  my_posts.pop(index_post)
  
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
  index_post = find_by_id(id)
  if index_post is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
  post_dict = post.model_dump()
  post_dict['id'] = id
  my_posts[index_post] = post_dict
  return {"data": post_dict}
  