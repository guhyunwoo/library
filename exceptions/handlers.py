from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from .business_exceptions import BusinessException, ValidationException
from .error_codes import ErrorCode, ErrorMessage

class ErrorResponse:
    def __init__(self, error_code: str, message: str, details: dict = None, status_code: int = 400):
        self.error_code = error_code
        self.message = message
        self.details = details or {}
        self.status_code = status_code
    
    def to_dict(self):
        return {
            "success": False,
            "error": {
                "code": self.error_code,
                "message": self.message,
                "details": self.details
            }
        }

async def business_exception_handler(request: Request, exc: BusinessException):
    status_code = 400 if isinstance(exc, ValidationException) else 422
    
    error_response = ErrorResponse(
        error_code=exc.error_code,
        message=exc.message,
        details=exc.details,
        status_code=status_code
    )
    
    return JSONResponse(
        status_code=status_code,
        content=error_response.to_dict()
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    error_response = ErrorResponse(
        error_code=ErrorCode.HTTP_ERROR.value,
        message=f"{ErrorMessage.HTTP_ERROR.value}: {exc.detail}",
        status_code=exc.status_code
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.to_dict()
    )

async def general_exception_handler(request: Request, exc: Exception):
    error_response = ErrorResponse(
        error_code=ErrorCode.INTERNAL_SERVER_ERROR.value,
        message=ErrorMessage.INTERNAL_SERVER_ERROR.value,
        status_code=HTTP_500_INTERNAL_SERVER_ERROR
    )
    
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content=error_response.to_dict()
    )

def setup_exception_handlers(app):
    app.add_exception_handler(BusinessException, business_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
