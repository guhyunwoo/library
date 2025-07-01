from . import con, cur, get_db
from exceptions.business_exceptions import DatabaseException
import sqlite3

def create_book(title: str, author: str):
    try:
        get_db()
        sql = "INSERT INTO books (title, author) VALUES (?, ?)"
        cur.execute(sql, (title, author))
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        raise DatabaseException(str(e), "create_book")

def get_available_books():
    try:
        get_db()
        sql = "SELECT title, author FROM books WHERE available = 1"
        cur.execute(sql)
        books = cur.fetchall()
        return [{"title": book[0], "author": book[1]} for book in books]
    except Exception as e:
        raise DatabaseException(str(e), "get_available_books")

def delete_book(book_id: int):
    try:
        get_db()
        sql = "SELECT title, available FROM books WHERE book_id = ?"
        cur.execute(sql, (book_id,))
        book_info = cur.fetchone()
        
        if not book_info or book_info[1] != 1:
            return False
        
        sql = "DELETE FROM books WHERE book_id = ?"
        cur.execute(sql, (book_id,))
        con.commit()
        return True
    except Exception as e:
        raise DatabaseException(str(e), "delete_book")