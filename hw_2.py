user_num = int(input("Enter a four-digit number: "))

valv_1 = user_num // 1000
valv_2 = (user_num - valv_1 * 1000) // 100
valv_3 = (user_num - valv_1 * 1000 - valv_2 * 100) // 10
valv_4 = user_num % 10

print(valv_1)
print(valv_2)
print(valv_3)
print(valv_4)
