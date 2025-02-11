from fastapi import APIRouter

imei_router = APIRouter(prefix="/imei_checker", tags=["IMEI Checker"])

from .v1 import v1_imei_router  # noqa
from .sandbox import sandbox_imei_router  # noqa

imei_router.include_router(v1_imei_router)
imei_router.include_router(sandbox_imei_router)
