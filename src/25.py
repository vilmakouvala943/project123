def calculate_average(numbers):
    if not numbers:
        raise ValueError("The list of numbers is empty")
    return sum(numbers) / len(numbers)
