from pprint import pprint

# creation
user = {
    "id": 22,
    "name": "Alex",
    "hobbies": ["tennis", "soccer"],
    "is_married": True,
    "address": {"city": "Odessa", "street": "Pobeda", "building": 15},
    "siblings": None,
    "money": 100,
}
user2 = dict(id=365, name="John")
user3 = dict(id=385, name="Marta", hobbies=None)

parcel = {}
parcel2 = dict()
raw_data_for_dict = [[5, 8], ["a", "a"]]
parcel3 = dict(raw_data_for_dict)
score = {0: ["Alex"], 20: ["Marta", "Jonh"], None: ["Alex2"]}


# get data

user_id = user["id"]
user2_id = user2["id"]

user_hobbies = user.get("hobbies", [])
user2_hobbies = user2.get("hobbies", [])
user3_hobbies = user3.get("hobbies") or []

# update
# list tape
user2["hobbies"] = ["diving"]
user2["hobbies"] = ["scuba"]
user2["hobbies"].append("diving")

# int tape
user["money"] += 150

# dict type

user["address"]["city"] = "Dnipro"
user["address"]["street"] = "Nezalezhnosti"
user["address"]["building"] = 17
# pprint(user, indent=4)

#
user_sddress = {
    "city": "Odessa",
    "street": "Pobeda",
    "building": 15,
}
user_data = {"id": 18, "city": "Kyiv"}

result_dict_option1 = {**user_sddress, **user_data}
result_dict_option2 = user_sddress | user_data
result_dict_option3 = user_sddress | user_data

# delete
# deleete all data in dict
result_dict_option1.clear()

# delete value by key

del result_dict_option2["street"]

city = result_dict_option2.pop("city")
city2 = result_dict_option2.pop("city2", "")

# iterate

# for elem in user:
#    print(elem, "-", user[elem])

for key, value in user.items():
    print(key)


atlethes = []
for elem in score.values():
    atlethes.extend(elem)
print(atlethes)


pass
