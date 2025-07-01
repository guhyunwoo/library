from fastapi import APIRouter
from pydantic import BaseModel
from service import books as service

router = APIRouter(prefix="/books")

class BookCreate(BaseModel):
    title: str
    author: str

# 1. 도서 등록
@router.post("")
def create_book(book: BookCreate):
    return service.create_book(book.title, book.author)

# 2. 대출 가능한 도서 목록 조회
@router.get("")
def get_available_books():
    return service.get_available_books()

# 3. 도서 삭제
@router.delete("/{book_id}")
def delete_book(book_id: int):
    return service.delete_book(book_id)
