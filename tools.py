import os
import random
import string
from pathlib import Path

CYR_LOWERCASE = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def remove_test_dir(dir_path):
    Path(dir_path).mkdir(parents=True, exist_ok=True)
    if os.path.isdir(dir_path):
        for f in os.listdir(dir_path):
            if not f.endswith(".mp4") and not f.endswith(".png") and not f.endswith(".txt"):
                continue
            else:
                try:
                    os.remove(os.path.join(dir_path, f))
                except FileNotFoundError:
                    pass


def random_word(min_len, max_len, first_letter="", capitalized=True):
    word = first_letter + "".join(random.choice(CYR_LOWERCASE) for _ in range(random.randrange(min_len, max_len + 1)))
    if capitalized:
        word = word.capitalize()
    return word

def get_email():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) + '@gmail.com'