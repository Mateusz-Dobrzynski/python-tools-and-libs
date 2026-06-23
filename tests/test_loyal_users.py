from datetime import date

from src.debugging.main import is_loyal


users = [
    {
        "username": "Alice",
        "join_date": date(2024, 5, 15),
    },
    {
        "username": "Bob",
        "join_date": date(2025, 2, 21),
    },
    {
        "username": "Mallory",
        "join_date": date(2023, 4, 21),
    },
]


def test_loyal_users():
    for user in users:
        assert not is_loyal(user)
