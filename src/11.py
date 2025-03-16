import random
def get_random_code(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    for i in range(n):
        code += alphabet[random.randint(0, 25)]
    return code