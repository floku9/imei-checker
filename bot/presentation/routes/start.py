from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, User

from application.dto.auth import RegistryUserDTO
from application.services.registration import RegistrationService
from utils.exceptions import RequestException
from utils.messages import Messages

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message, registration_service: RegistrationService):
    user: User = message.from_user  # noqa
    user_dto = RegistryUserDTO(
        telegram_id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )

    try:
        await registration_service.register_user(user_dto)
        await message.answer(Messages.USER_SUCCESSFULLY_REGISTERED)
    except RequestException as e:
        match e.status_code:
            case 409:
                await message.answer(Messages.USER_ALREADY_REGISTERED)
