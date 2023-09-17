import secrets
class Middle_square:

    def __init__(self, min, max):
        self.max = max
        self.min = min
        print("hpsssssjjjjjjjjjjjjj")
        self.seed = secrets.randbits(64)    # Genera un número aleatorio seguro como un long

    def middle_square(self):
        print(self.seed)
       # random_numbers = []
       # for i in range(10):
        # Elevamos la semilla al cuadrado
        squared = self.seed * self.seed
            # Convertimos el resultado en una cadena para trabajar con los dígitos
        squared_str = str(squared)
        print(f"{len(squared_str)}     j")
            # Aseguramos que la cadena tenga al menos 8 dígitos

        print(f"{len(squared_str)}     j22")
        print(squared_str)
            # Tomamos los dígitos centrales (de la posición 2 a la 6)
        middle = squared_str[int((len(squared_str)/2))-2:int((len(squared_str)/2))+2]
        print(f"{middle}  {int((len(squared_str)/2))-2}  {int((len(squared_str)/2))+2}    {len(squared_str)}")
            # Convertimos los dígitos centrales en un número entero
        new_seed = int(middle)/10000.0
            # Guardamos el nuevo número en la lista de números aleatorios
            #random_numbers.append(new_seed)
            # La semilla para la próxima iteración es el nuevo número
        middle = middle.zfill(8)
        self.seed = int (middle)

        return new_seed
    """def generate_random_number(self, size):
        if size <= 0:
            raise ValueError("El tamaño debe ser mayor que cero")

        # Generar bytes aleatorios usando secrets
        num_bytes = (size + 7) // 8  # Calcula la cantidad de bytes necesarios
        random_bytes = secrets.token_bytes(num_bytes)

        # Convierte los bytes en un número entero
        random_number = int.from_bytes(random_bytes, byteorder='big')

        # Ajusta el tamaño si es necesario
        random_number = random_number % (2 ** size)
        return random_number"""

    def generateNi(self):
        number = self.min + (self.max - self.min) * self.middle_square()
        print(number)
        return number

# Ejemplo de cómo generar un número de 16 bits (2 bytes)
"""random_num = generate_random_number(16)
print(random_num)s"" 

# Semilla inicial y cantidad de números pseudoaleatorios a generar
seed = 1234
n = 10

# Generar la secuencia de números pseudoaleatorios
random_sequence = middle_square(seed, n)

# Imprimir la secuencia generada
print(random_sequence)"""

m = Middle_square(0,1)
print(m.generateNi())
