import random

def get_random_code(length=8):
    """Generate a random code with the given length."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

print(get_random_code())
