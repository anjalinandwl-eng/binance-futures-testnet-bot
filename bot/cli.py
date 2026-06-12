from validators import *
from orders import *
from logging_config import logger


symbol = input("Enter Symbol: ").upper()

side = input("BUY or SELL: ").upper()

order_type = input("MARKET or LIMIT: ").upper()

quantity = float(input("Enter Quantity: "))


price = None

if order_type == "LIMIT":
    price = float(input("Enter Price: "))


try:

    validate_side(side)

    validate_order_type(order_type)

    validate_quantity(quantity)

    logger.info(
        f"Request -> {symbol} {side} {order_type} {quantity}"
    )

    if order_type == "MARKET":

        order = place_market_order(
            symbol,
            side,
            quantity
        )

    else:

        order = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )

    logger.info(order)

    print("\n===== ORDER SUCCESS =====")

    print("Order ID:", order["orderId"])

    print("Status:", order["status"])

    print("Executed Qty:", order["executedQty"])

except Exception as e:

    logger.error(str(e))

    print("ERROR:", e)
