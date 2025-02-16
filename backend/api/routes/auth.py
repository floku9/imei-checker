from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from api.dependencies import get_users_service, get_whitelist_service
from api.dto.auth import UserDetailDTO, UserCreateDTO, TokenResponseDTO
from application.services.repository.users import UsersService
from application.services.repository.whitelist import WhitelistService
from utils.jwt_utils import create_jwt_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get("/get_token_by_tg_id/{telegram_id}", response_model=TokenResponseDTO)
async def get_token_by_telegram_id(
    telegram_id: int,
    whitelist_service: WhitelistService = Depends(get_whitelist_service),
    users_service: UsersService = Depends(get_users_service),
) -> TokenResponseDTO:
    user = await users_service.get_by_telegram_id(telegram_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if not await whitelist_service.is_user_whitelisted(user.telegram_id):
        raise HTTPException(status_code=401, detail="User is not whitelisted")

    jwt = create_jwt_token({"user_id": telegram_id}, expires_delta=timedelta(seconds=5))
    return TokenResponseDTO(token=jwt)


@router.post("/add_tg_user", response_model=UserCreateDTO)
async def add_telegram_user(
    user: UserDetailDTO,
    users_service: UsersService = Depends(get_users_service),
) -> UserCreateDTO:
    user_in_db = await users_service.get_by_telegram_id(user.telegram_id)
    if user_in_db:
        raise HTTPException(status_code=409, detail="User already exists")
    return await users_service.add_telegram_user(user)
