import random

class Uniform:
    def __init__(self, quantity, min_value, max_value):
        self.quantity = quantity
        self.min_value = min_value
        self.max_value = max_value
        self.aleatory = []

    def get_aleatory(self):
        self.generate_random()
        return self.aleatory

    def generate_random(self):
        while self.quantity > 0:
            random_number = random.uniform(self.min_value, self.max_value)
            self.aleatory.append(random_number)
            self.quantity -= 1

"""if __name__ == "__main__":
    min_value = 0  
    max_value = 10  
    quantity = 10  
    uniform_generator = Uniform(quantity, min_value, max_value)
    aleatory_numbers = uniform_generator.get_aleatory()
    print(aleatory_numbers)"""
