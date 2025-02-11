from backend.api.dto.base import BaseDTO


class AuthorizationResponseDTO(BaseDTO):
    token: str
