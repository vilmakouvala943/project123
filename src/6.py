def get_random_number(n):
    import random
    return random.randint(1, n)

def get_prime_factors(n):
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def get_random_prime(n):
    while True:
        prime = get_random_number(n)
        if is_prime(prime):
            return prime

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
