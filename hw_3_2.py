lst = [12, 3, 4, 10, 8]
if len(lst) > 1:
    elm = lst.pop()
    lst.insert(0, elm)
    print(lst)
else:
    print(lst)
