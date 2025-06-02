from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


app = FastAPI()

@app.get('/blog')
def index(limit=10, published:bool=True, sort: Optional[str]=None):
    # Only get 10 published blogs
    if published:
        return {'Data': f'{limit} form the DB'}
    else:
        return {'Data': 'All blogs form the DB'}

@app.get('/about')
def about():
    return "About Page"

@app.get('/contact')
def contact():
    return

@app.get('/blog/unpublished')
def unpublished():
    return {'Data': 'All unpublished Blog'}


@app.get('/blog/{id}')
def blog(id: int):
    return {'Data': id}

@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return {'Data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
@app.post('/blog')
def create_blog(blog: Blog):
 
    return {'Data': f'Blog is Created with title as {blog.title}'}


# if __name__ =="__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)