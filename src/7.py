
import random

def get_random_code():
    numbers = "0123456789"
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-=+[]{}|;':\"<>,./?`~"
    code = ""
    for i in range(12):
        code += random.choice(numbers)
    for i in range(6):
        code += random.choice(characters)
    for i in range(3):
        code += random.choice(special_characters)
    return code