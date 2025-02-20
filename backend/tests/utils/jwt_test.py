from datetime import timedelta
from jwt import ExpiredSignatureError, InvalidTokenError
import pytest

from utils.jwt_utils import create_jwt_token, decode_jwt_token


@pytest.fixture
def jwt_data() -> dict:
    return {"user_id": 123}


def test_create_jwt_token(jwt_data: dict):
    jwt = create_jwt_token(data=jwt_data, expires_delta=timedelta(seconds=5))
    assert jwt is not None


def test_token_expiration(jwt_data: dict):
    jwt = create_jwt_token(data=jwt_data, expires_delta=timedelta(seconds=-1))
    with pytest.raises(ExpiredSignatureError):
        decode_jwt_token(jwt)


def test_invalid_token():
    token = "booba"
    with pytest.raises(InvalidTokenError):
        decode_jwt_token(token)
