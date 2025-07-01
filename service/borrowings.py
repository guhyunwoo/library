from data import borrowings as data
from cache import borrower as cache
from exceptions.business_exceptions import *
import re

def borrow_book(borrower: str, title: str):
    if not borrower or not borrower.strip():
        raise RequiredFieldException("대출자명")
    
    if not title or not title.strip():
        raise RequiredFieldException("도서 제목")
    
    borrower = borrower.strip()
    title = title.strip()
    
    result = data.borrow_book(borrower, title)
    
    if not result:
        raise BookNotAvailableException(title)
    
    cache.add_borrower_book(borrower, title)
    return result

def get_monthly_borrows(borrow_month: str):
    if not borrow_month or not borrow_month.strip():
        raise RequiredFieldException("대출 월")
    
    borrow_month = borrow_month.strip()
    
    if not re.match(r'^\d{4}-\d{2}$', borrow_month):
        raise InvalidDateFormatException(borrow_month)
    
    year, month = borrow_month.split('-')
    year, month = int(year), int(month)
    
    if year < 2000 or year > 2100:
        raise InvalidFieldException("년도", str(year), "2000-2100 사이")
    
    if month < 1 or month > 12:
        raise InvalidFieldException("월", str(month), "01-12 사이")
    
    return data.get_monthly_borrows(borrow_month)

def get_borrower_books(borrower: str):
    if not borrower or not borrower.strip():
        raise RequiredFieldException("대출자명")
    
    borrower = borrower.strip()
    books = cache.get_borrower_books(borrower)
    
    return {
        "borrower": borrower,
        "books": books
    }

def return_book(borrower: str, title: str):
    if not borrower or not borrower.strip():
        raise RequiredFieldException("대출자명")
    
    if not title or not title.strip():
        raise RequiredFieldException("도서 제목")
    
    borrower = borrower.strip()
    title = title.strip()
    
    result = data.return_book(borrower, title)
    
    if not result:
        raise BorrowNotFoundException(borrower, title)
    
    cache.remove_borrower_book(borrower, title)
    return result
