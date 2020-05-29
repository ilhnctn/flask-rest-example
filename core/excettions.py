from typing import Optional


class BaseError(Exception):
    def __init__(self, code: Optional[int] = None, message: Optional[str] = None) -> None:
        super(BaseError, self).__init__()
        self.message = message
        self.code = code


class BaseApiError(BaseError):
    def __init__(self, status_code: Optional[int] = None) -> None:
        super(BaseApiError, self).__init__()
        self.status_code = status_code
