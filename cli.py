import argparse

from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)",
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order Side",
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type",
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity",
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Limit Price (Required for LIMIT orders)",
    )

    args = parser.parse_args()

    try:
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\n" + "=" * 50)
        print("ORDER REQUEST")
        print("=" * 50)

        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type == "LIMIT":
            print(f"Price       : {price}")

        print("\nSubmitting order...\n")

        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print("=" * 50)
        print("ORDER RESPONSE")
        print("=" * 50)

        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")

        avg_price = response.get("avgPrice")

        if not avg_price or avg_price == "0.00000":
            avg_price = "Not Available"

        print(f"Average Price : {avg_price}")

        print("\n✅ Order placed successfully!")

    except Exception as e:
        print("\n❌ Order Failed")
        print(f"Reason: {e}")


if __name__ == "__main__":
    main()