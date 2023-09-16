import secrets
class Middle_square:

    def __init__(self, min, max):
        self.max = max
        self.min = min
        self.seed = secrets.randbelow(9223372036854775807)  # Genera un número aleatorio seguro como un long

    def middle_square(self):
        random_numbers = []
        for i in range(10):

            # Elevamos la semilla al cuadrado
            squared = self.seed * self.seed
            # Convertimos el resultado en una cadena para trabajar con los dígitos
            squared_str = str(squared)
            # Aseguramos que la cadena tenga al menos 8 dígitos
            squared_str = squared_str.zfill(8)
            # Tomamos los dígitos centrales (de la posición 2 a la 6)
            middle = squared_str[2:6]
            # Convertimos los dígitos centrales en un número entero
            new_seed = int(middle)
            # Guardamos el nuevo número en la lista de números aleatorios
            random_numbers.append(new_seed)
            # La semilla para la próxima iteración es el nuevo número
            seed = new_seed
        return random_numbers
"""
# Semilla inicial y cantidad de números pseudoaleatorios a generar
seed = 1234
n = 10

# Generar la secuencia de números pseudoaleatorios
random_sequence = middle_square(seed, n)

# Imprimir la secuencia generada
print(random_sequence)"""

m = Middle_square(10,20)
print(m.middle_square())