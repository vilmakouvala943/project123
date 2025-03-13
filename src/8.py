def get_random_string(length):
    import random
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result

get_random_string(10)
