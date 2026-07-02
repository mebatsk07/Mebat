import sys
from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
)

logger.add(
    "logs/btc_engine.log",
    rotation="10 MB",
    retention="30 days",
    level="INFO",
)

__all__ = ["logger"]