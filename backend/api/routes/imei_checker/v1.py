from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query

from backend.api.dependencies import get_imei_checker_service
from backend.api.dto.imei_checker import ImeiInfoDTO
from backend.api.security import get_current_user
from backend.application.services.imei_checker.api_based import APIImeiCheckerService
from backend.utils.constants import IMEI_REGEX
from backend.utils.exceptions import RequestException

v1_imei_router = APIRouter(prefix="/v1", tags=["IMEI Checker", "v1"])


@v1_imei_router.get("/check/", response_model=ImeiInfoDTO)
async def check(
    imei: Annotated[str, Query(pattern=IMEI_REGEX)],
    imei_checker_service: APIImeiCheckerService = Depends(get_imei_checker_service),
    user_id: int = Depends(get_current_user),
) -> ImeiInfoDTO:
    try:
        return await imei_checker_service.receive_info_about_imei(imei=imei)
    except RequestException as e:
        match e.status_code:
            case 402:
                raise HTTPException(
                    503,
                    detail="For now service for receiving information about IMEI is unavailable. Please contact support.",
                )
            case 422:
                raise HTTPException(404, detail="IMEI is not valid")
            case _:
                raise e
