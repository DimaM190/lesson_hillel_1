# some_string = "I Live in Odessa since 2004"
#
# other_result = some_string.split("i")
# other_result_visual = ["I", "Live", "in", "Odessa", "since", "2004"]
# empty_list = []
# not_empty_list = ["444", 5555, 5.5, True, False, [55], empty_list]
# if not_empty_list:
#     print(5555)
#
#
# fifth_elem = not_empty_list[4]
# # big_elem = not_empty_list[40]
# fifth_letter = some_string[4]
#
# len_list = len(not_empty_list)
# len_list2 = len(empty_list)
# len_string = len(some_string)

###########################################

purchase_plan = ["banana"]

# add 1 element
purchase_plan.append("salt")
purchase_plan.append("salt")
purchase_plan.append("2")

# marge by another list
sister_plan = ["bread", "milk"]
purchase_plan.extend(sister_plan)
# purchase_plan.extend("4454545rgerg4545454")

# purchase_plan.sort()
# purchase_plan.sort(reverse=True)
purchase_plan.sort(key=len)


# delete item

purchase_plan.remove("salt")
if "nails" in purchase_plan:
    purchase_plan.remove("nails")

if "abc" in "abcdd":
    print(363635)

# delete by index
purchase_plan.pop()
purchase_plan.pop(0)


pass
