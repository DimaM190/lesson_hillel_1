import decimal
import logging

from pywebio.input import slider, FLOAT, NUMBER
from pywebio.input import input as pw_input
from pywebio.output import put_html, put_success, put_error


import shop_clients

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop_1.log"), logging.StreamHandler()],
)
# PRICES
APPLE_PRICE = decimal.Decimal(str(52.75))
BANANA_PRICE = decimal.Decimal(str(81.40))

# HEADER
put_html("<h1>Welcome to our Fruit Shop</h1>")

user_id = pw_input("Enter your ID", required=True)
user_id = user_id.strip()

if user_id in shop_clients.CLIENTS or shop_clients.OPEN_DOOR_DAY:
    apple_weight = slider(
        "Apples", type=FLOAT, min_value=0, max_value=5, value=0.01, required=True
    )
    banana_weight = pw_input(
        "Bananas", type=NUMBER, required=True, min=0, max=10, value=0
    )
    apple_weight = decimal.Decimal(apple_weight).quantize(
        decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
    )
    banana_weight = decimal.Decimal(banana_weight).quantize(
        decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
    )

    logging.info(f"\n\tapple_weight= {apple_weight}\n\tbanana_weight= {banana_weight}")

    apple_cost = (APPLE_PRICE * apple_weight).quantize(
        decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
    )
    banana_cost = (BANANA_PRICE * banana_weight).quantize(
        decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
    )

    total_cost = apple_cost + banana_cost
    put_success(
        f"Total cost: \nApples cost\t{apple_cost} UAH\nBananas cost\t{banana_cost} UAH\nTotal cost\t\t{total_cost} UAH"
    )
else:
    put_error("Wrong ID. Please register ")
    new_client_id = pw_input("Enter yuor ID").strip()
    shop_clients.CLIENTS.append(new_client_id)
    registered_users = ",\n".join(shop_clients.CLIENTS)
    put_success(registered_users)
