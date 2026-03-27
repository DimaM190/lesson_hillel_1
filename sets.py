from enum import unique

some_list = [55, 656, 898, 55, 55, "Alex"]
some_list2 = [55, 656, 898, 55, 55, 11111111111111, "Alex", "5"]
some_iterable = "lkdhflejhfflkjehf4g5lj4f86heglr"
target_dict = {}
for elem in some_list:
    target_dict[elem] = None
print(target_dict.keys())


unique_elem = set(some_list)
print(unique_elem)

created_set = {555, 4545, 555}
created_set2 = set()
created_set3 = set(some_iterable)

is_5_in_createg_set3 = "5" in created_set3
is_5_not_in_some_list2 = "5" not in some_list2

# adding
created_set.add("555555555555555")
created_set.add((3,))

# remove
created_set.remove(4545)
created_set.discard(2222)

# сравнения

set1 = set(some_list)


pass
