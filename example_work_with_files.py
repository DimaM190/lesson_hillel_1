# my_file = open("game.py")
# my_file.close()


# # когда открываем текстовый файл обязательно указывать mode ='r', encoding='utf-8' ---  только  чтение
# with open("game.py", mode="r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# запись в файл mode="w" - каждый раз перезаписывается
# number = 665
# with open("schop_plan.txt", mode="w", encoding="utf-8") as file:
#     for position in range(10 + 1):
#         file.write(f"data:{position}\n")
#     file.write("the end")

# запись в файл mode="a" - данные до записываются
# number = 665
# with open("schop_plan.txt", mode="a", encoding="utf-8") as file:
#     for position in range(10 + 1):
#         file.write(f"data:{position}\n")
#     file.write("the end")
