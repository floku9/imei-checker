import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from presentation.dependencies import registration_service, token_service
from presentation.routes.start import start_router
from settings import bot_settings, redis_settings

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Initialize bot and dispatcher
bot = Bot(token=bot_settings.BOT_TOKEN)

# Initialize dispatcher with dependency injection and redis storage for FSM
redis_storage = RedisStorage.from_url(redis_settings.REDIS_URL)
dp = Dispatcher(
    token_service=token_service, registration_service=registration_service, storage=redis_storage
)

# Include routers
dp.include_router(start_router)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
