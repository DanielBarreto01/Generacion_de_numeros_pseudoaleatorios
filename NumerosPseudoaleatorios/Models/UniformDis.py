import random

class Uniform:
    def __init__(self, quantity, min_value, max_value):
        self.quantity = quantity
        self.min_value = min_value
        self.max_value = max_value
        self.aleatory = []
        self.ri_sequence = []
        self.ni_sequence = []

    def get_aleatory(self):
         # Genera números pseudoaleatorios y los devuelve
        self.generate_random()
        return self.aleatory

    def generate_random(self):
        while self.quantity > 0:
              # Genera un número pseudoaleatorio uniformemente distribuido en el rango [min_value, max_value]
            random_number = random.uniform(self.min_value, self.max_value)
            self.aleatory.append(random_number)
            xi = float(random_number) / 10000.0  # Convierte el número aleatorio en xi
            self.ni_sequence.append(xi)
            # Calcula el valor de xi (escala el número aleatorio al rango [0, 1))
            ni = self.min_value + (self.max_value - self.min_value) * xi
            self.ni_sequence.append(ni)
            self.ri_sequence.append(xi)
            self.quantity -= 1

    def getrRi(self):
        
        return self.ri_sequence

if __name__ == "__main__":
    min_value = 0 
    max_value = 1 
    quantity = 2 
    uniform_generator = Uniform(quantity, min_value, max_value)
    aleatory_numbers = uniform_generator.get_aleatory()
    print("semilla",aleatory_numbers)
    print("Ri",uniform_generator.ri_sequence)
    print("Ni",uniform_generator.ni_sequence)
