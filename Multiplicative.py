class Multiplicative:
    def __init__(self, x, t, g, quantity):
        self.x = x
        self.a = (8 * t) + 3
        self.m = 2 ** g
        self.aleatory = []
        self.quantity = quantity
        self.seeds = []

    def get_aleatory(self):
        self.generate_random(self.calculate_seed(self.x))
        return self.aleatory

    def generate_random(self, seed):
        while len(self.aleatory) < self.quantity:
            self.aleatory.append(self.calculate_number(seed))
            new_seed = self.calculate_seed(seed)
            self.seeds.append(seed)
            seed = new_seed

    def calculate_number(self, seed):
        return seed / (self.m - 1)

    def calculate_seed(self, xi):
        return (xi * self.a) % self.m

    def get_seeds(self):
        return self.seeds


# Ejemplo de uso
if __name__ == "__main__":
    x = 12345
    t = 7
    g = 15
    quantity = 10

    rng = Multiplicative(x, t, g, quantity)
    aleatory_numbers = rng.get_aleatory()
    seeds = rng.get_seeds()

    print("Números Aleatorios:")
    for i, num in enumerate(aleatory_numbers):
        print(f"R{i+1}: {num:.6f}")

    print("\nSemillas:")
    for i, seed in enumerate(seeds):
        print(f"Seed{i+1}: {seed}")
