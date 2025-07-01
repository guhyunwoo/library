from . import redis_client

def test():
    try:
        redis_client.ping()
        return "redis connect ok"
    except:
        return "redis connect failed"

def add_borrower_book(borrower: str, title: str):
    try:
        key = f"borrower:{borrower}:books"
        redis_client.sadd(key, title)
        return True
    except:
        return False

def get_borrower_books(borrower: str):
    try:
        key = f"borrower:{borrower}:books"
        books = redis_client.smembers(key)
        return [book.decode('utf-8') for book in books]
    except:
        return []

    try:
        key = f"borrower:{borrower}:books"
        redis_client.srem(key, title)
        return True
    except:
        return False
