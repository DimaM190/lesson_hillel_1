import json

user = {
    "id": 22,
    "name": "Олександр",
    "hobbies": ["tennis", "soccer"],
    "is_married": True,
    "address": {"city": "Odessa", "street": "Pobeda", "building": 15},
    "siblings": None,
    "money": 100,
}

# dict to string
result_string = json.dumps(user, ensure_ascii=False)

# string to dict

recover_dict = json.loads(result_string)

# dict to file

with open("useer.json", mode="w", encoding="utf-8") as file:
    # json.dump(user, file, indent=4, ensure_ascii=False)
    json.dump(user, file, indent=4)

# file into dict
with open("useer.json", mode="r", encoding="utf-8") as file:
    discover_from_file = json.load(file)

pass
