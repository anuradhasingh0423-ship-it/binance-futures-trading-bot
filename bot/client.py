import os
import time

from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException

from bot.logging_config import logger

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def get_client():
    try:
        client = Client(
            API_KEY,
            API_SECRET,
            testnet=True,
        )

        # Futures Testnet URL
        client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        # Synchronize local timestamp with Binance server
        server_time = client.get_server_time()
        client.timestamp_offset = (
            server_time["serverTime"] - int(time.time() * 1000)
        )

        logger.info("Connected to Binance Futures Testnet")

        return client

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Connection Error: {e}")
        raise