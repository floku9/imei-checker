from backend.api.dto.imei_checker import ImeiInfoDTO
from backend.application.services.imei_checker.base import BaseImeiCheckerService
from backend.application.interactors.imei_checker_client.base import BaseImeiCheckerClient


class SandboxImeiCheckerService(BaseImeiCheckerService):
    def __init__(self, imei_checker_client: BaseImeiCheckerClient) -> None:
        self.imei_checker_client = imei_checker_client

    async def receive_info_about_imei(self, imei: str) -> ImeiInfoDTO:
        info = await self.imei_checker_client.check_imei(imei)
        return ImeiInfoDTO(**info)
