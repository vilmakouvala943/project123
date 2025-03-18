 import random
import string
import re

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def get_random_code():
    code = generate_random_string(8)
    while not re.match("^[a-zA-Z0-9]*$", code):
        code = generate_random_string(8)
    return code