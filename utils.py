import requests

from constans import URL


def get_json_data(entity_name: str) -> list[dict]:
    url = f"{URL}{entity_name}"
    params = {"limit": 50000}
    response = requests.get(url, params=params)
    response_json = response.json()
    entities = response_json[entity_name]
    return entities


def get_user_contact_data(user: dict) -> dict:
    return user


def get_users_in_state(state: str) -> list[dict]:
    users = get_json_data("users")
    users_in_state = []
    for user in users:
        if user["address"]["state"] == state:
            users_in_state.append(user)
    return users_in_state
