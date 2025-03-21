import random

def create_random_string(length):
    """
    Generate a random string of given length.
    
    Parameters:
        - length (int): The length of the generated string.
    
    Returns:
        - str: A randomly generated string of the specified length.
    """
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

random_string = create_random_string(10)
print(random_string)
