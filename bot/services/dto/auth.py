from services.dto.base import BaseDTO


class RegistryUserDTO(BaseDTO):
    telegram_id: int
    username: str
    first_name:  str
    last_name: str