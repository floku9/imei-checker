from datetime import timedelta, datetime, timezone
from typing import Optional
from settings import jwt_settings
import jwt


def create_jwt_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    if expires_delta is None:
        expires_delta = timedelta(minutes=jwt_settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": datetime.now(tz=timezone.utc) + expires_delta, "iat": datetime.now(tz=timezone.utc)})
    return jwt.encode(to_encode, jwt_settings.JWT_SECRET_KEY, algorithm=jwt_settings.JWT_ALGORITHM)


def decode_jwt_token(token: str) -> dict:
    return jwt.decode(token, jwt_settings.JWT_SECRET_KEY, algorithms=[jwt_settings.JWT_ALGORITHM])
