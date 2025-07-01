from data import books as data
from exceptions.business_exceptions import *

def create_book(title: str, author: str):
    if not title or not title.strip():
        raise RequiredFieldException("도서 제목")
    
    if not author or not author.strip():
        raise RequiredFieldException("저자명")
    
    title = title.strip()
    author = author.strip()
    
    result = data.create_book(title, author)
    
    if not result:
        raise BookAlreadyExistsException(title)
    
    return result

def get_available_books():
    return data.get_available_books()

def delete_book(book_id: int):
    if not isinstance(book_id, int) or book_id <= 0:
        raise InvalidFieldException("도서 ID", str(book_id), "양의 정수")
    
    result = data.delete_book(book_id)
    
    if not result:
        raise BookNotFoundException(f"ID: {book_id}")
    
    return result
