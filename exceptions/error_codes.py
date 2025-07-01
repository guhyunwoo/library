from enum import Enum

class ErrorCode(Enum):
    """에러 코드 정의"""
    
    # 일반 에러
    BUSINESS_ERROR = "BUSINESS_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"
    CACHE_ERROR = "CACHE_ERROR"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    HTTP_ERROR = "HTTP_ERROR"
    
    # 도서 관련 에러
    BOOK_NOT_FOUND = "BOOK_NOT_FOUND"
    BOOK_NOT_AVAILABLE = "BOOK_NOT_AVAILABLE"
    BOOK_ALREADY_EXISTS = "BOOK_ALREADY_EXISTS"
    
    # 대출 관련 에러
    BORROW_NOT_FOUND = "BORROW_NOT_FOUND"
    ALREADY_BORROWED = "ALREADY_BORROWED"
    
    # 입력 검증 에러
    INVALID_DATE_FORMAT = "INVALID_DATE_FORMAT"
    REQUIRED_FIELD_MISSING = "REQUIRED_FIELD_MISSING"
    INVALID_FIELD_VALUE = "INVALID_FIELD_VALUE"

class ErrorMessage(Enum):
    """에러 메시지 정의 (한국어)"""
    
    # 일반 에러 메시지
    BUSINESS_ERROR = "비즈니스 로직 오류가 발생했습니다"
    VALIDATION_ERROR = "입력값 검증에 실패했습니다"
    DATABASE_ERROR = "데이터베이스 오류가 발생했습니다"
    CACHE_ERROR = "캐시 시스템 오류가 발생했습니다"
    INTERNAL_SERVER_ERROR = "예상치 못한 서버 오류가 발생했습니다"
    HTTP_ERROR = "HTTP 요청 처리 중 오류가 발생했습니다"
    
    # 도서 관련 메시지
    BOOK_NOT_FOUND = "요청하신 도서를 찾을 수 없습니다"
    BOOK_NOT_AVAILABLE = "해당 도서는 현재 대출이 불가능합니다"
    BOOK_ALREADY_EXISTS = "이미 등록된 도서입니다"
    
    # 대출 관련 메시지
    BORROW_NOT_FOUND = "대출 기록을 찾을 수 없습니다"
    ALREADY_BORROWED = "이미 대출 중인 도서입니다"
    
    # 입력 검증 메시지
    INVALID_DATE_FORMAT = "날짜 형식이 올바르지 않습니다"
    REQUIRED_FIELD_MISSING = "필수 입력값이 누락되었습니다"
    INVALID_FIELD_VALUE = "입력값이 올바르지 않습니다"
    
    # 성공 메시지
    BOOK_CREATED = "도서가 성공적으로 등록되었습니다"
    BOOK_DELETED = "도서가 성공적으로 삭제되었습니다"
    BOOK_BORROWED = "도서 대출이 완료되었습니다"
    BOOK_RETURNED = "도서 반납이 완료되었습니다"
    BOOKS_RETRIEVED = "도서 목록을 성공적으로 조회했습니다"
    BORROWS_RETRIEVED = "대출 기록을 성공적으로 조회했습니다"
    BORROWER_BOOKS_RETRIEVED = "대출자의 도서 목록을 성공적으로 조회했습니다"
