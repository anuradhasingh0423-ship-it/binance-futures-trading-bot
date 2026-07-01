from binance.exceptions import BinanceAPIException

from bot.client import get_client
from bot.logging_config import logger

client = get_client()


def place_order(symbol, side, order_type, quantity, price=None):
    """
    Place a Market or Limit order on Binance Futures Testnet.
    """

    try:
        logger.info(
            f"Order Request | Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
            )

        else:
            raise ValueError("Invalid order type.")

        logger.info(f"Create Order Response: {response}")

        # Fetch updated order details
        order_details = client.futures_get_order(
            symbol=symbol,
            orderId=response["orderId"],
        )

        logger.info(f"Order Details: {order_details}")

        return order_details

    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        raise

    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        raise