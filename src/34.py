import math

def calculate_sums(values):
    total_sum = sum(values)
    square_sum = sum(x ** 2 for x in values)
    squared_values_sum = [x ** 2 for x in values]
    squared_sum = sum(squared_values_sum)

    return {
        "total_sum": total_sum,
        "square_sum": square_sum,
        "squared_values_sum": squared_values_sum
    }
