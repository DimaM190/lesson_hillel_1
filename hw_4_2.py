list1 = [0, 1, 7, 2, 4, 8]
list2 = [1, 2, 5]
list3 = [6]
list4 = []

lst = list2
total_sum = 0
elm = len(lst)
# last_elm = lst[-1]
if elm == 0:
    print(0)
else:
    for index_list, element_list in enumerate(lst):
        if index_list % 2 == 0:
            total_sum += element_list

    print(total_sum * lst[-1])


pass
