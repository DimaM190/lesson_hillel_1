list_1 = [0, 1, 0, 12, 3]
list_2 = [0]
list_3 = [1, 0, 13, 0, 0, 0, 5]
list_4 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

list_r = []
list_l = []

for number in list_4:
    if number == 0:
        list_l.append(number)
    else:
        list_r.append(number)

list_final = list_r + list_l
print(list_final)
