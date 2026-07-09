import json


PROFILE_PATH = "data/user_profile.json"


def load_user_data():
    with open(PROFILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def save_user_data(data):
    with open(PROFILE_PATH, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )