def get_random_string(length=8):
    import random
    import string
    characters = "".join([random.choice(string.ascii_letters) for _ in range(length)])
    return characters

get_random_string()
