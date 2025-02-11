from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException
from backend.api.dependencies import get_telegram_users_service, get_whitelist_service
from backend.api.dto.authorization import AuthorizationResponseDTO
from backend.application.services.repository.users import UsersService
from backend.application.services.repository.whitelist import WhitelistService
from backend.utils.jwt_utils import create_jwt_token

router = APIRouter(prefix="/authorization", tags=["Authorization"])


@router.get("/{telegram_id}", response_model=AuthorizationResponseDTO)
async def authorize_by_telegram_id(
    telegram_id: int,
    whitelist_service: WhitelistService = Depends(get_whitelist_service),
    telegram_users_service: UsersService = Depends(get_telegram_users_service),
):
    user = await telegram_users_service.get_by_telegram_id(telegram_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    if not await whitelist_service.is_user_whitelisted(user.id):
        raise HTTPException(status_code=401, detail="User is not whitelisted")

    jwt = create_jwt_token({"user_id": telegram_id}, expires_delta=timedelta(seconds=5))
    return AuthorizationResponseDTO(token=jwt)
