from loguru import logger
import sys


# Configure loguru
logger.remove()  # Remove default handler
logger.add(
    sys.stdout,  # Output to console
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>",
    colorize=True,  # Enable colors in console
    level="DEBUG",  # Set logging level
)


# Make logger available throughout the project
def get_logger():
    return logger
