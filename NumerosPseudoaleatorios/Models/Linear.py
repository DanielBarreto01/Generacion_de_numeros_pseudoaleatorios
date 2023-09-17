import math

class Linear:
    def __init__(self, x, k, c, g, quantity, interval_start=0, interval_end=1):
        # Inicializa los valores necesarios para el generador lineal congruencial
        self.x = x
        self.a = 1 + 2 * k
        self.c = c
        self.m = 2 ** g
        self.aleatory = [] # Almacena los números pseudoaleatorios generados
        self.quantity = quantity # Cantidad de números a generar
        self.interval_start = interval_start
        self.interval_end = interval_end
        self.seeds = [] # Almacena las semillas utilizadas
        self.ri_sequence = [] # Almacena la secuencia de valores Ri

    def get_aleatory(self):
          # Genera números pseudoaleatorios y los devuelve
        self.generate_random(self.calculate_seed(self.x))
        return self.aleatory

    def generate_random(self, seed):
        # Genera números pseudoaleatorios recursivamente hasta alcanzar la cantidad deseada
        if len(self.aleatory) < self.quantity:
            random_number = self.calculate_number(seed)
            mapped_number = self.map_to_interval(random_number)
            self.aleatory.append(mapped_number)
            self.ri_sequence.append(mapped_number)  # Agrega el valor individual a ri_sequence
            new_seed = self.calculate_seed(seed)
            self.seeds.append(seed)
            self.generate_random(new_seed)

    def calculate_number(self, seed):
         # Calcula un número pseudoaleatorio en el rango [0, 1)
        return float(seed) / (self.m - 1)

    def calculate_seed(self, xi):
        # Calcula la siguiente semilla en la secuencia
        return (self.a * xi + self.c) % self.m

    def map_to_interval(self, number):
        # Mapea el número pseudoaleatorio al intervalo deseado
        return self.interval_start + (number * (self.interval_end - self.interval_start))

    
    def get_seeds(self):
        # Devuelve las semillas utilizadas
        return self.seeds
    
    def getRi(self):
         # Devuelve la secuencia de valores Ri
        return self.ri_sequence
    
    def getNi(self):
        # Devuelve la secuencia de números pseudoaleatorios generados
        return self.aleatory

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
for i, random_number in enumerate(random_numbers):
    print(f'R{i + 1} = {random_number:.6f}')

