import numpy as np

def calculate_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("The list of numbers cannot be empty")
    
    mean = sum(numbers) / len(numbers)
    return mean

numbers = [1.5, 2.7, 3.8, 4.1]
print(calculate_mean(numbers))
