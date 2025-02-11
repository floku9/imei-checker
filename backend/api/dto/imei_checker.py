from backend.api.dto.base import BaseDTO


class ImeiInfoDTO(BaseDTO):
    imei: str
    info: list[dict[str, object]]
