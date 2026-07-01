import logging
import os


# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)


def setup_logger():
    logger = logging.getLogger("TradingBot")

    # Prevent duplicate log messages
    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler("logs/trading.log")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


logger = setup_logger()