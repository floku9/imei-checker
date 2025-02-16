from api.dto.imei_checker import ImeiInfoDTO
from application.services.imei_checker.base import BaseAPIImeiCheckerService


class APIImeiCheckerService(BaseAPIImeiCheckerService):
    async def receive_info_about_imei(self, imei: str) -> ImeiInfoDTO:
        async with self.imei_checker_client as client:
            raw_result = await client.check_imei(imei)
            properties = raw_result["properties"]
            return ImeiInfoDTO(imei=imei, info=properties)
