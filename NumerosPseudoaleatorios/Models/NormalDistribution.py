import random
import math

class NormalDistribution:
    def __init__(self, mu, sigma, quantity):
        self.mu = mu
        self.sigma = sigma
        self.quantity = quantity
        self.aleatory = []
        self.xi_sequence = []
        self.ri_sequence = []
        self.ni_sequence = []

    def get_aleatory(self):
        # Genera números pseudoaleatorios y los devuelve
        self.generate_random()
        return self.aleatory

    def generate_random(self):
        # Genera dos números pseudoaleatorios uniformemente distribuidos en el rango [0, 1)
        while self.quantity > 0:
            u1 = random.random()
            u2 = random.random()
             # Aplica la transformación de Box-Muller para obtener un número aleatorio con distribución normal
            z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
            random_number = self.mu + z0 * self.sigma
            self.aleatory.append(random_number)

            # Calcular Xi, Ri y Ni y almacenarlos
            xi = random.uniform(self.mu - 3 * self.sigma, self.mu + 3 * self.sigma)
            self.xi_sequence.append(xi)
            ri = (random_number - self.mu) / self.sigma
            self.ri_sequence.append(ri)
            ni = self.mu + xi * self.sigma
            self.ni_sequence.append(ni)

            self.quantity -= 1

    def getXi(self):
        # Devuelve la secuencia de valores Xi o semillas
        return self.xi_sequence

    def getRi(self):
        # Devuelve la secuencia de valores Ri
        return self.ri_sequence

    def getNi(self):
        # Devuelve la secuencia de valores Ni
        return self.ni_sequence

# Ejemplo de uso
if __name__ == "__main__":
    mu = 0  # Media
    sigma = 1  # Desviación estándar
    quantity = 10  # Cantidad de números pseudoaleatorios a generar

    rng = NormalDistribution(mu, sigma, quantity)
    aleatory_numbers = rng.get_aleatory()
    xi_sequence = rng.getXi()
    ri_sequence = rng.getRi()
    ni_sequence = rng.getNi()

    print("Números Aleatorios Distribución Normal:")
    for i, num in enumerate(aleatory_numbers):
        print(f"X{i+1}: {num:.6f}")

    print("\nValores de Xi:")
    for i, xi in enumerate(xi_sequence):
        print(f"Xi{i+1}: {xi:.6f}")

    print("\nValores de Ri:")
    for i, ri in enumerate(ri_sequence):
        print(f"Ri{i+1}: {ri:.6f}")

    print("\nValores de Ni:")
    for i, ni in enumerate(ni_sequence):
        print(f"Ni{i+1}: {ni:.6f}")
