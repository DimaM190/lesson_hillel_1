im_num1 = input("Enter the first number: ").strip()
act = input("Enter action(+; -; *; /): ").strip()
im_num2 = input("Enter the second number: ").strip()

num1 = float(im_num1)
num2 = float(im_num2)

if act == "+":
    print(num1 + num2)
elif act == "-":
    print(num1 - num2)
elif act == "*":
    print(num1 * num2)
elif act == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("You can't divide by 0!!!")
else:
    print("Something went wrong!!!")
