from typing import Annotated
from fastapi import APIRouter, Depends, Query

from backend.api.dependencies import get_sandbox_imei_checker_service
from backend.api.dto.imei_checker import ImeiInfoDTO
from backend.api.security import get_current_user
from backend.application.services.imei_checker.sandbox import SandboxImeiCheckerService
from backend.utils.constants import IMEI_REGEX

sandbox_imei_router = APIRouter(prefix="/sandbox", tags=["IMEI Checker", "sandbox"])


@sandbox_imei_router.get("/check/", response_model=ImeiInfoDTO)
async def check(
    imei: Annotated[str, Query(pattern=IMEI_REGEX)],
    imei_checker_service: SandboxImeiCheckerService = Depends(get_sandbox_imei_checker_service),
    user_id: int = Depends(get_current_user),
) -> ImeiInfoDTO:
    return await imei_checker_service.receive_info_about_imei(imei=imei)
