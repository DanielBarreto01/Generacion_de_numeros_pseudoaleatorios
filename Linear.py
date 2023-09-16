import math

class Linear:
    def __init__(self, x, k, c, g, quantity, interval_start=0, interval_end=1):
        self.x = x
        self.a = 1 + 2 * k
        self.c = c
        self.m = 2 ** g
        self.aleatory = []
        self.quantity = quantity
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.seeds = []

    def get_aleatory(self):
        self.generate_random(self.calculate_seed(self.x))
        return self.aleatory

    def generate_random(self, seed):
        if len(self.aleatory) < self.quantity:
            random_number = self.calculate_number(seed)
            mapped_number = self.map_to_interval(random_number)
            self.aleatory.append(mapped_number)
            new_seed = self.calculate_seed(seed)
            self.seeds.append(seed)
            self.generate_random(new_seed)

    def calculate_number(self, seed):
        return float(seed) / (self.m - 1)

    def calculate_seed(self, xi):
        return (self.a * xi + self.c) % self.m

    def map_to_interval(self, number):
        return self.interval_start + (number * (self.interval_end - self.interval_start))

    def get_seeds(self):
        return self.seeds

# Ejemplo de uso:
x = 42
k = 5
c = 17
g = 32
quantity = 10
interval_start = 0
interval_end = 10

linear_generator = Linear(x, k, c, g, quantity, interval_start, interval_end)

random_numbers = linear_generator.get_aleatory()
seeds = linear_generator.get_seeds()

print("Números aleatorios:", random_numbers)
print("Semillas utilizadas:", seeds)
