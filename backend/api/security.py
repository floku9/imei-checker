from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_utils import decode_jwt_token
import jwt

bearer = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Security(bearer)) -> int:
    try:
        token = credentials.credentials
        payload = decode_jwt_token(token)
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
