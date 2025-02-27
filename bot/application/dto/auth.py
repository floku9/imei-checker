from typing import Optional

from application.dto.base import BaseDTO


class RegistryUserDTO(BaseDTO):
    telegram_id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]


class GetTokenDTO(BaseDTO):
    token: str
