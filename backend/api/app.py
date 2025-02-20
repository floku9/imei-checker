import logging
from fastapi import FastAPI
import uvicorn
from api.routes.auth import router as auth_router
from api.routes.imei_checker.base import imei_router

app = FastAPI(
    title="IMEI Checker API",
    description="API for checking IMEIs",
    version="0.1.0",
    docs_url="/docs",
)
app.include_router(auth_router)
app.include_router(imei_router)


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

