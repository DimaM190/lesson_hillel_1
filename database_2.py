import os
import constans_2
import json


def setup_database() -> None:
    """create database connection"""
    database_name = constans_2.DATABASE_NAME
    if os.path.exists(database_name):
        return
    with open(database_name, mode="w", encoding="utf-8") as database_file:
        json.dump([], database_file)


def get_users() -> list[dict]:
    with open(constans_2.DATABASE_NAME, encoding="utf-8") as storage:
        return json.load(storage)
