import abc
from backend.api.dto.imei_checker import ImeiInfoDTO
from backend.application.interactors.imei_checker_client.base import BaseAPIImeiCheckerClient


class BaseImeiCheckerService(abc.ABC):
    @abc.abstractmethod
    async def receive_info_about_imei(self, imei: str) -> ImeiInfoDTO:
        raise NotImplementedError


class BaseAPIImeiCheckerService(BaseImeiCheckerService):

    def __init__(self, imei_checker_client: BaseAPIImeiCheckerClient):
        self.imei_checker_client = imei_checker_client

    @abc.abstractmethod
    async def receive_info_about_imei(self, imei: str) -> ImeiInfoDTO:
        raise NotImplementedError
