from typing import Optional
from .error_codes import ErrorCode, ErrorMessage

class BusinessException(Exception):
    """비즈니스 로직 예외 기본 클래스"""
    
    def __init__(self, message: str, error_code: ErrorCode = ErrorCode.BUSINESS_ERROR, details: Optional[dict] = None):
        self.message = message
        self.error_code = error_code.value
        self.details = details or {}
        super().__init__(self.message)

class ValidationException(BusinessException):
    """입력 검증 예외"""
    
    def __init__(self, message: str, field: Optional[str] = None):
        super().__init__(
            message=message,
            error_code=ErrorCode.VALIDATION_ERROR,
            details={"field": field} if field else {}
        )

class BookNotFoundException(BusinessException):
    """도서를 찾을 수 없음 예외"""
    
    def __init__(self, book_identifier: str):
        super().__init__(
            message=f"{ErrorMessage.BOOK_NOT_FOUND.value}: {book_identifier}",
            error_code=ErrorCode.BOOK_NOT_FOUND,
            details={"book_identifier": book_identifier}
        )

class BookNotAvailableException(BusinessException):
    """도서 대출 불가 예외"""
    
    def __init__(self, title: str, reason: str = "이미 대출된 상태입니다"):
        super().__init__(
            message=f"{ErrorMessage.BOOK_NOT_AVAILABLE.value}: '{title}' - {reason}",
            error_code=ErrorCode.BOOK_NOT_AVAILABLE,
            details={"title": title, "reason": reason}
        )

class BookAlreadyExistsException(BusinessException):
    """도서 중복 등록 예외"""
    
    def __init__(self, title: str):
        super().__init__(
            message=f"{ErrorMessage.BOOK_ALREADY_EXISTS.value}: '{title}'",
            error_code=ErrorCode.BOOK_ALREADY_EXISTS,
            details={"title": title}
        )

class BorrowNotFoundException(BusinessException):
    """대출 기록을 찾을 수 없음 예외"""
    
    def __init__(self, borrower: str, title: str):
        super().__init__(
            message=f"{ErrorMessage.BORROW_NOT_FOUND.value}: 대출자 '{borrower}', 도서 '{title}'",
            error_code=ErrorCode.BORROW_NOT_FOUND,
            details={"borrower": borrower, "title": title}
        )

class AlreadyBorrowedException(BusinessException):
    """이미 대출된 상태 예외"""
    
    def __init__(self, borrower: str, title: str):
        super().__init__(
            message=f"{ErrorMessage.ALREADY_BORROWED.value}: 대출자 '{borrower}', 도서 '{title}'",
            error_code=ErrorCode.ALREADY_BORROWED,
            details={"borrower": borrower, "title": title}
        )

class DatabaseException(BusinessException):
    """데이터베이스 관련 예외"""
    
    def __init__(self, message: str, operation: str):
        super().__init__(
            message=f"{ErrorMessage.DATABASE_ERROR.value} ({operation}): {message}",
            error_code=ErrorCode.DATABASE_ERROR,
            details={"operation": operation}
        )

class CacheException(BusinessException):
    """캐시 관련 예외"""
    
    def __init__(self, message: str, operation: str):
        super().__init__(
            message=f"{ErrorMessage.CACHE_ERROR.value} ({operation}): {message}",
            error_code=ErrorCode.CACHE_ERROR,
            details={"operation": operation}
        )

class InvalidDateFormatException(ValidationException):
    """잘못된 날짜 형식 예외"""
    
    def __init__(self, date_value: str, expected_format: str = "YYYY-MM"):
        super().__init__(
            message=f"{ErrorMessage.INVALID_DATE_FORMAT.value}: '{date_value}' (예상 형식: {expected_format})",
            field="date"
        )
        self.details.update({"date_value": date_value, "expected_format": expected_format})

class RequiredFieldException(ValidationException):
    """필수 필드 누락 예외"""
    
    def __init__(self, field_name: str):
        super().__init__(
            message=f"{ErrorMessage.REQUIRED_FIELD_MISSING.value}: {field_name}",
            field=field_name
        )

class InvalidFieldException(ValidationException):
    """잘못된 필드 값 예외"""
    
    def __init__(self, field_name: str, value: str, expected: str = ""):
        expected_msg = f" (예상값: {expected})" if expected else ""
        super().__init__(
            message=f"{ErrorMessage.INVALID_FIELD_VALUE.value}: {field_name} = '{value}'{expected_msg}",
            field=field_name
        )
        self.details.update({"value": value, "expected": expected})
