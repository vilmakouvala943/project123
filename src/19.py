import random

class RandomGenerator:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.append(data)

    def get_random_data(self):
        if not self.data:
            raise ValueError("No data to generate")
        
        return random.choice(self.data)
