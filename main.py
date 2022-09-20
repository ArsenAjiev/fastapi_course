from fastapi import FastAPI, Query, Path, Body
from schemas import Book
from typing import List

app = FastAPI()

#
# @app.get('/')
# def home():
#     return {"key": "Hello"}
#
#
# @app.get('/{pk}')
# def get_iem(pk: int, q: str = None):
#     return {"key": pk, "q": q}
#
#
# @app.get('/user/{pk}/item/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}


@app.post('/book')
def create_book(item: Book = Body(..., embed=True), quantity: int = Body(...)):
    return item, quantity


@app.get('/book')
def get_book(q: List[str] = Query("test", description="search book", deprecated=True)):
    return q


@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10)):
    return {"pk": pk, "pages": pages}