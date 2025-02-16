from typing import Optional, Union
from api.dto.base import BaseDTO


class TokenResponseDTO(BaseDTO):
    token: str


class UserDetailDTO(BaseDTO):
    telegram_id: int
    username: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]


class UserCreateDTO(BaseDTO):
    id: Union[int, str]


class UserUpdateDTO(UserDetailDTO):
    pass
