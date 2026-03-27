user_input = input("Please enter a number between 0 and 8640000: ")

day = divmod(int(user_input), 24 * 60 * 60)
hours = divmod(day[1], 60 * 60)
minute = divmod(hours[1], 60)

if 11 <= day[0] % 100 <= 14:
    day_format = "днів"
elif day[0] % 10 == 1:
    day_format = "день"
elif 2 <= day[0] % 10 <= 4:
    day_format = "дні"
else:
    day_format = "днів"

print(f"{day[0]} {day_format}, {hours[0]}:{minute[0]}:{minute[1]}")
print(15 % 100)
