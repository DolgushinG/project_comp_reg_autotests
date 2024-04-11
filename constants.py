import os
from dataclasses import dataclass

import tools
username = "climb" #stands for !@user
password = "tester" #stands for ^&pass
webpage = "climbing-events.ru"

URL = 'http://{}:{}@{}'.format(username, password, webpage)

@dataclass
class User:
    firstname: str = tools.random_word(4, 8)
    lastname: str = tools.random_word(4, 8)
    email: str = tools.get_email()
    password: str = "password"
    birthday: str = "20202905"
    team: str = "team"
    city: str = "Москва"
    gender: str = "Male"


DEFAULT_USER = User(
    email="Tester@tester.ru",
    password="password",
)
