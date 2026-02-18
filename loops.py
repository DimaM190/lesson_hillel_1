from pprint import pprint

some_list = [55, 666] * 6
some_string = "bfgb54554654rgr54535"
products = ["banana", "vodka", "milk", "dread", "vodka"]

for product in products:

    if product == "milk":
        break

    if product == "vodka":
        continue

    print(product)
    if product == "vodka":
        print("No boozy today")

print(888888)


people = [
    ["Alex", "Bush", "Odesa", 35, True, 34134],
    ["Petr", "Kovalsky", "Odesa", 35, True, 3973],
    ["Alex", "Bush", "Kyiv, Lobanovska str", 65, False, 693234],
    ["Alex", "Bush", "Odesa", 35, True, 6353224],
    ["Petr", "Kovalsky", "Odesa", 35, True, 4694164],
    ["Olga", "Butterfly", "KYIV", 22, False, 25426],
    ["Alex", "Bush", "Odesa", 35, True, 324656],
    ["Petr", "Kovalsky", "Odesa", 35, True, 62366826],
    ["Olga", "Butterfly", "Kyiv", 22, False, 264264342],
]
# all married people
# not marid from Kyiv
# average adge of married people

all_married_people = []
not_married_from_city = []
city = "Kyiv"

total_age = 0

############################################################
for person in people:
    # person ['Alex', 'Bush', 'Odesa', 35, True, 34134]
    name, surname, address, age, is_married, inn = person
    # is_married = person[4]
    # address = person[2].lower()
    if is_married:
        all_married_people.append(person)
    if not is_married and city.lower() in address.lower():
        not_married_from_city.append(person)
if all_married_people:
    ages = []
    for married_person in all_married_people:
        age = married_person[3]
        total_age += age
        # option 2
        ages.append(age)

    print(f"Average age of married = {total_age/len(all_married_people)}")
    print(f"Average age of married = {sum(ages)/len(all_married_people)}")
else:
    print("no married")


print("all married")
pprint(all_married_people)
print(f"not married from {city}")
pprint(not_married_from_city)
############################################################

#
# for person in people:
#     # person ['Alex', 'Bush', 'Odesa', 35, True, 34134]
#     is_married = person[4]
#     if is_married:
#         all_married_people.append(person)
# pprint(all_married_people)
#
#
# not_married_from_city = []
# city = "Kyiv"
# for person in people:
#     # person ['Alex', 'Bush', 'Odesa', 35, True, 34134]
#     is_married = person[4]
#     address = person[2].lower()
#     if not is_married and city.lower() in address:
#         not_married_from_city.append(person)
# pprint(not_married_from_city)


# WARNING
list_string = "123"
print(id(list_string))
for number in list_string:
    print(number)
    print(id(list_string))
    new_number = int(number) * 2
    list_string += str(new_number)


# list_data = [55, 66]
# for number in list_data:
#     print(number)
#     new_number = number * 2
#     list_data.append(new_number)
