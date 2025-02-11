from fastapi import FastAPI
import uvicorn
from backend.api.routes.authorization import router as auth_router
from backend.api.routes.imei_checker.base import imei_router

app = FastAPI(
    title="IMEI Checker API",
    description="API for checking IMEIs",
    version="0.1.0",
    docs_url="/docs",
)
app.include_router(auth_router)
app.include_router(imei_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
