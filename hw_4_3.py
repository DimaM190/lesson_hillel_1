import random

my_list = []
for element in range(random.randint(3, 10)):
    my_list.append(random.randint(1, 1000))
print(my_list)
element1 = my_list[0]
element2 = my_list[2]
element3 = my_list[-2]
final_list = [element1, element2, element3]
print(final_list)

# так правильнее писать случайный список из случайных элементов
my_list_1 = [random.randint(1, 100) for i in range(random.randint(6, 15))]
print(my_list_1)
