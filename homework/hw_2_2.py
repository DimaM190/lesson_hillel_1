user_input = int(input("enter a five-digit integer: "))

valv1 = user_input % 10
number1 = user_input // 10
valv2 = number1 % 10
number2 = number1 // 10
valv3 = number2 % 10
number3 = number2 // 10
valv4 = number3 % 10
valv5 = user_input // 10000
print(valv1 * 10000 + valv2 * 1000 + valv3 * 100 + valv4 * 10 + valv5)
