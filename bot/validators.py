def validate_side(side):

    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid Side")


def validate_order_type(order_type):

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid Order Type")


def validate_quantity(quantity):

    if float(quantity) <= 0:
        raise ValueError("Quantity must be greater than 0")
