from fastapi import FastAPI
from web import borrowings as borrow_web
from web import books as book_web
from exceptions.handlers import setup_exception_handlers

app = FastAPI(
    title="도서 대출 관리 시스템",
    description="Library Management System API",
    version="1.0.0"
)

setup_exception_handlers(app)

app.include_router(book_web.router)
app.include_router(borrow_web.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', reload=True)
