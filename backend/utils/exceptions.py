from typing import Any, Optional


class RequestException(Exception):
    def __init__(self, status_code: int, error_info: Optional[dict] = None):
        self.status_code = status_code
        self.error_info = error_info
        super().__init__()

    def __repr__(self):
        return (
            f"RequestException("
            f"status_code={self.status_code}, "
            f"detail={repr(self.detail)}, "
            f"error_info={repr(self.error_info)})"
        )

    def __str__(self):
        return f"Status Code: {self.status_code}, Error Info: {self.error_info}"
