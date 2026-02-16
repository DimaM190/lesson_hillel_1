from pywebio.input import slider, FLOAT, NUMBER
from pywebio.input import input as pw_input

from pywebio.output import put_html

CHEESE_PRICE = 286.35
POTATO_PRICE = 40.32

# HEADER
put_html("<h1>Welcome to uor shop</h1>")

# INPUT SELECTION

cheese_eight = slider(
    "Cheese", type=FLOAT, min_value=0, max_value=5, value=0.15, required=True
)

potato_weight = pw_input("Potato", type=NUMBER, required=True, min=0, max=10, value=3)
pass
