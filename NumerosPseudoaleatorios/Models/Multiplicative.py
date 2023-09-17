class Multiplicative:
    def __init__(self, x, t, g, quantity):
        self.x = x  # Semilla inicial
        self.a = (8 * t) + 3  # Semilla inicial
        self.m = 2 ** g  # Semilla inicial
        self.aleatory = []  # Almacena los números pseudoaleatorios generados
        self.quantity = quantity # Almacena los números pseudoaleatorios generados
        self.ri_sequence = []   # Almacena la secuencia de valores Ri
        self.seeds = [] # Almacena las semillas utilizadas

    def get_aleatory(self):
         # Genera números pseudoaleatorios y los devuelve
        self.generate_random(self.calculate_seed(self.x))
        return self.aleatory

    def generate_random(self, seed):
        # Genera números pseudoaleatorios hasta alcanzar la cantidad deseada
        while len(self.aleatory) < self.quantity:
            self.aleatory.append(self.calculate_number(seed))
            self.ri_sequence.append(self.calculate_number(seed))
            new_seed = self.calculate_seed(seed)
            self.seeds.append(seed)
            seed = new_seed

    def calculate_number(self, seed):
        # Calcula un número pseudoaleatorio en el rango [0, 1)
        return seed / (self.m - 1)

    def calculate_seed(self, xi):
        # Calcula la siguiente semilla en la secuencia
        return (xi * self.a) % self.m

    def get_seeds(self):
         # Devuelve las semillas utilizadas
        return self.seeds
    
    def getRi(self):
         # Devuelve las semillas utilizadas
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
