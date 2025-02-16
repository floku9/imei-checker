from application.interactors.imei_checker_client.base import BaseImeiCheckerClient


class SandboxImeiCheckerClient(BaseImeiCheckerClient):
    async def check_imei(self, imei: str) -> dict:
        return {"imei": imei, "info": [{"gratz": "this is good imei, thank you, mate"}]}


sandbox_imei_checker_client = SandboxImeiCheckerClient()
