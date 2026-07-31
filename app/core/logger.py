import sys
from loguru import logger
from app.core.config import get_settings

settings = get_settings()


def setup_logger():
    logger.remove()  # hapus default handler

    # Console — colorful output
    logger.add(
        sys.stdout,
        level=settings.log_level,
        format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan> - <white>{message}</white>",
        colorize=True,
    )

    # File — rotate harian, simpan 7 hari
    logger.add(
        "./logs/app.log",
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="1 day",
        retention="7 days",
        compression="zip",
    )

    return logger


app_logger = setup_logger()
