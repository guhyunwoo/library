from . import con, cur, get_db
from exceptions.business_exceptions import DatabaseException
import sqlite3

def borrow_book(borrower: str, title: str):
    try:
        get_db()
        
        sql = "SELECT book_id FROM books WHERE title = ? AND available = 1"
        cur.execute(sql, (title,))
        book = cur.fetchone()
        
        if not book:
            return False
        
        book_id = book[0]
        
        sql = "SELECT borrow_id FROM borrowings WHERE book_id = ? AND borrower = ? AND returned_at IS NULL"
        cur.execute(sql, (book_id, borrower))
        existing_borrow = cur.fetchone()
        
        if existing_borrow:
            return False
        
        sql = "INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)"
        cur.execute(sql, (book_id, borrower))
        
        sql = "UPDATE books SET available = 0 WHERE book_id = ?"
        cur.execute(sql, (book_id,))
        
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        raise DatabaseException(str(e), "borrow_book")

def get_monthly_borrows(borrow_month: str):
    try:
        get_db()
        sql = """
        SELECT b.borrower, bk.title, bk.author 
        FROM borrowings b 
        JOIN books bk ON b.book_id = bk.book_id 
        WHERE strftime('%Y-%m', b.borrowed_at) = ?
        """
        cur.execute(sql, (borrow_month,))
        borrows = cur.fetchall()
        return [{"borrower": borrow[0], "title": borrow[1], "author": borrow[2]} for borrow in borrows]
    except Exception as e:
        raise DatabaseException(str(e), "get_monthly_borrows")

def return_book(borrower: str, title: str):
    try:
        get_db()
        
        sql = """
        SELECT b.borrow_id, b.book_id 
        FROM borrowings b 
        JOIN books bk ON b.book_id = bk.book_id 
        WHERE b.borrower = ? AND bk.title = ? AND b.returned_at IS NULL
        """
        cur.execute(sql, (borrower, title))
        borrow = cur.fetchone()
        
        if not borrow:
            return False
        
        borrow_id, book_id = borrow
        
        sql = "UPDATE borrowings SET returned_at = current_timestamp WHERE borrow_id = ?"
        cur.execute(sql, (borrow_id,))
        
        sql = "UPDATE books SET available = 1 WHERE book_id = ?"
        cur.execute(sql, (book_id,))
        
        con.commit()
        return True
    except Exception as e:
        raise DatabaseException(str(e), "return_book")

def test():
    try:
        get_db()
        return "sqlite connect ok"
    except Exception as e:
        raise DatabaseException(str(e), "test_connection")
