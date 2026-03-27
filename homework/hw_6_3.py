user_num = input("enter number:")

while int(user_num) > 9:
    result = 1

    for num in user_num:
        result *= int(num)

    user_num = str(result)

print(user_num)
