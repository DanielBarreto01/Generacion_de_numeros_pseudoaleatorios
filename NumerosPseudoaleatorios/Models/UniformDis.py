import random

class Uniform:
    def __init__(self, quantity):
        self.quantity = quantity
        self.aleatory = []

    def get_aleatory(self):
        self.generate_random()
        return self.aleatory

    def generate_random(self):
        while self.quantity > 0:
            self.aleatory.append(random.random())
            self.quantity -= 1

# Ejemplo de uso
if __name__ == "__main__":
    uniform_generator = Uniform(10)  # Cambia 10 por la cantidad deseada
    aleatory_numbers = uniform_generator.get_aleatory()
    print(aleatory_numbers)
