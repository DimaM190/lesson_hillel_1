from utils import (
    get_unique_values,
    get_division,
    validate_not_hashable,
    send_email_manager,
)

my_unique_values1 = get_unique_values("some_itersble")
my_unique_values2 = get_unique_values([])
my_unique_values3 = get_unique_values({5, 6})

validate_not_hashable(5)
send_email_manager()

fraсtion = get_division(10, 0)
print(fraсtion)
