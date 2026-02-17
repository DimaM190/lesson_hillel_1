# lst = [1, 2, 3, 4, 5, 6]
# lst = [1, 2, 3]
# lst = [1]
# lst = [1, 2, 3, 4, 5]
lst = [1]
num_el = len(lst)
if num_el == 0:
    lst1 = [[], []]
    print(lst1)
elif num_el % 2 == 0:
    lst_l = lst[: (num_el // 2)]
    lst_r = lst[num_el // 2 :]
    lst1 = [lst_l, lst_r]
    print(lst1)
elif num_el == 1:
    lst1 = [lst, []]
    print(lst1)
else:
    lst_l = lst[: ((num_el + 1) // 2)]
    lst_r = lst[((num_el + 1) // 2) :]
    lst1 = [lst_l, lst_r]
    print(lst1)
