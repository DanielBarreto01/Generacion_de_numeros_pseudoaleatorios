import secrets

class Middle_square:
    def __init__(self, min_value, max_value, quantity):
        self.quantity = quantity
        self.xi_sequence = []  # Almacena los valores de Xi (conjunto semilla)
        self.ri_sequence = [] 
        self.ni_sequence = []
        self.max = max_value
        self.min = min_value
        self.seed = self.generate_random_number(25)  # Genera un número aleatorio seguro como un long

    def middle_square(self):
        ni_sequence = []
        for _ in range(self.quantity):
            # Elevamos la semilla al cuadrado
            squared = self.seed * self.seed
            # Convertimos el resultado en una cadena para trabajar con los dígitos
            squared_str = str(squared)
            # Aseguramos que la cadena tenga al menos 8 dígitos
            squared_str = squared_str.zfill(8)
            # Tomamos los dígitos centrales (de la posición 2 a la 6)
            middle = squared_str[int((len(squared_str) / 2)) - 2:int((len(squared_str) / 2)) + 2]
            # Convertimos los dígitos centrales en un número entero
            new_seed = float(middle) / 10000.0
            # Guardamos el nuevo número en la lista de números aleatorios
            ni_sequence.append(new_seed)
            # La semilla para la próxima iteración es el nuevo número
            self.seed = int(middle)
            # Calculamos Ni (número pseudoaleatorio en un intervalo determinado)
            ni = self.min + (self.max - self.min) * new_seed
            # Guardamos los valores correspondientes en las secuencias
            self.xi_sequence.append(self.seed)
            self.ri_sequence.append(new_seed)
            self.ni_sequence.append(ni)
            # La semilla para la próxima iteración es el nuevo número
            self.seed = int(middle)
        return ni_sequence

    def generate_random_number(self, size):
        if size <= 0:
            raise ValueError("El tamaño debe ser mayor que cero")

        # Generar bytes aleatorios usando secrets
        num_bytes = (size + 7) // 8  # Calcula la cantidad de bytes necesarios
        random_bytes = secrets.token_bytes(num_bytes)

        # Convierte los bytes en un número entero
        random_number = int.from_bytes(random_bytes, byteorder='big')

        # Ajusta el tamaño si es necesario
        random_number = random_number % (2 ** size)

        return random_number
    
    def getRi(self):
        return self.ri_sequence
    def getXi(self):
        return self.xi_sequence

# Ejemplo de uso:
min_value = 0  # Ajusta los valores de min y max según tus necesidades
max_value = 1
quantity = 10  # Cantidad de números pseudoaleatorios a generar

m = Middle_square(min_value, max_value, quantity)
random_sequence = m.middle_square()

# Imprimir la secuencia generada
print("Xi (Conjunto Semilla):", m.xi_sequence)
print("Ri (Número Pseudoaleatorio en [0,1]):",[f'{ri:.10f}' for ri in m.ri_sequence])
print("Ni (Número Pseudoaleatorio en un intervalo determinado):", m.ni_sequence)
