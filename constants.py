import os
from dataclasses import dataclass

import tools

URL = 'http://127.0.0.1:8000'


@dataclass
class User:
    firstname: str = tools.random_word(4, 8)
    lastname: str = tools.random_word(4, 8)
    email: str = tools.get_email()
    password: str = "password"
    birthday: str = "password"
    team: str = "team"
    city: str = "Москва"
    gender: str = "Male"


DEFAULT_USER = User(
    email="Tester@tester.ru",
    password="password",
)
