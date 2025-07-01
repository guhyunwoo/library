from fastapi import APIRouter
from pydantic import BaseModel
from service import borrowings as service

router = APIRouter()

class BorrowRequest(BaseModel):
    borrower: str
    title: str

class ReturnRequest(BaseModel):
    borrower: str
    title: str

# 4. 도서 대출 처리
@router.post("/borrows")
def borrow_book(request: BorrowRequest):
    return service.borrow_book(request.borrower, request.title)

# 6. 특정 월 대출 기록 조회
@router.get("/borrows/month/{borrow_month}")
def get_monthly_borrows(borrow_month: str):
    return service.get_monthly_borrows(borrow_month)

# 7. 대출자 기록 조회
@router.get("/borrowers/{borrower}/books")
def get_borrower_books(borrower: str):
    return service.get_borrower_books(borrower)

# 8. 도서 반납 처리
@router.post("/return")
def return_book(request: ReturnRequest):
    return service.return_book(request.borrower, request.title)
