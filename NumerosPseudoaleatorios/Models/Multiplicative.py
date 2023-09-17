class Multiplicative:
    def __init__(self, x, t, g, quantity):
        self.x = x
        self.a = (8 * t) + 3
        self.m = 2 ** g
        self.aleatory = []
        self.quantity = quantity
        self.ri_sequence = [] 
        self.seeds = []

    def get_aleatory(self):
        self.generate_random(self.calculate_seed(self.x))
        return self.aleatory

    def generate_random(self, seed):
        while len(self.aleatory) < self.quantity:
            self.aleatory.append(self.calculate_number(seed))
            self.ri_sequence.append(self.calculate_number(seed))
            new_seed = self.calculate_seed(seed)
            self.seeds.append(seed)
            seed = new_seed

    def calculate_number(self, seed):
        return seed / (self.m - 1)

    def calculate_seed(self, xi):
        return (xi * self.a) % self.m

    def get_seeds(self):
        return self.seeds
    def getRi(self):
        return self.ri_sequence


# Ejemplo de uso
if __name__ == "__main__":
    x = 1
    t = 1
    g = 6
    quantity = 10

    rng = Multiplicative(x, t, g, quantity)
    aleatory_numbers = rng.get_aleatory()
    seeds = rng.get_seeds()
    ri_sequence = rng.ri_sequence

    print("Números Aleatorios:")
    for i, num in enumerate(aleatory_numbers):
        print(f"R{i+1}: {num:.6f}")

    print("\nSecuencia de Ri:")
    for i, ri in enumerate(ri_sequence):
        print(f"Ri{i+1}: {ri:.10f}")

    print("\nSemillas:")
    for i, seed in enumerate(seeds):
        print(f"Seed{i+1}: {seed}")
