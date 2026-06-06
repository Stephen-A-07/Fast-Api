

from fastapi import  FastAPI, HTTPException, Response,status,Depends
import psycopg2
from sqlalchemy.orm import Session
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas
from .database import  engine,get_db

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
  


#if both the path are same and the methods are also same then the first get method is considered order matters.

@app.get("/")
async def root():
  return {"message":"Welcome to my api"}

@app.get("/posts",response_model=list[schemas.Post])
def get_posts(db:Session = Depends(get_db)):
  # cursor.execute("""SELECT * FROM posts""")
  # posts = cursor.fetchall()
   
  posts = db.query(models.Post).all()
  return posts

#post methods

@app.post("/posts",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session = Depends(get_db)):
  # cursor.execute("""INSERT INTO posts 
  #                (title,content,published) VALUES(%s,%s,%s) RETURNING *""",
  #                (post.title,post.content,post.published)
  #                )
  # new_post = cursor.fetchone()
  # conn.commit()
  new_post = models.Post(**post.model_dump())
  
  db.add(new_post)
  db.commit()
  db.refresh(new_post)
  
  return new_post


@app.get("/posts/{id}",response_model=schemas.Post)
def get_post(id:int,db:Session = Depends(get_db)):
  # cursor.execute("""SELECT * FROM posts WHERE id=%s""",(str(id)))
  # post = cursor.fetchone()
  
  post = db.query(models.Post).filter(models.Post.id == id).first()
  
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
  return post


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(get_db)):
  # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""",(str(id)))
  # deleted_post = cursor.fetchone()
  # conn.commit()
  post = db.query(models.Post).filter(models.Post.id == id)
  
  if post.first() is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
  post.delete(synchronize_session = False)
  db.commit()
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}",response_model=schemas.Post)
def update_post(id:int,updated_post:schemas.PostCreate,db:Session = Depends(get_db)):
  # cursor.execute("""UPDATE posts SET title = %s,content = %s,published = %s WHERE id= %s returning *""",(post.title,post.content,post.published,str(id)))
  # updated_post = cursor.fetchone()
  # conn.commit()
  
  post_query = db.query(models.Post).filter(models.Post.id == id)
  
  post = post_query.first()
  if post is None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
  post_query.update(updated_post.model_dump(),synchronize_session = False)
  db.commit()
  return {post_query.first()}
  
  
  
@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
  new_user = models.User(**user.model_dump())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  
  return new_user