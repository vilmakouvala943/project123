import random

def simple_math_operations():
    """
    A simple math game where you are given two numbers and need to perform some operations on them.
    
    The possible operations are:
    - Addition (+)
    - Subtraction (-)
    - Multiplication (*)
    - Division (/)
    
    You can choose any number of operations to perform. If no operation is chosen, the program will default to addition with its operands.
    """
    # Example input numbers
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    print(f"Operation: {random.choice(['Addition', 'Subtraction', 'Multiplication', 'Division'])}")
    
    if random.choice([True, False]):
        result = num1 + num2
    elif random.choice([True, False]):
        result = num1 - num2
    elif random.choice([True, False]):
        result = num1 * num2
    else:
        result = num1 / num2

    print(f"The final result is: {result}")

simple_math_operations()
