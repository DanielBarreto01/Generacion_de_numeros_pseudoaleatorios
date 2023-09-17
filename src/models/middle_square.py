import secrets

class Middle_square:
    def __init__(self, min, max):
        self.seed = secrets.randbits(64)
        self.min = min
        self.max = max

    def middle_square(self):
        # Calculate the square of the seed
        square = self.seed * self.seed
        # Convert the square to a string with leading zeros
        square_str = str(square).zfill(12)
        # Get the length of the string and calculate the indices
        size = len(square_str)
        start = int(((size) / 2)-2)
        end = start + 4
        # Extract the characters representing the middle number
        number_str = square_str[start:end]
        # Convert the string to a numeric value and divide it by 10000 to get a number
        # in the range [0, 1)
        number = float(number_str) / 10000.0
        # Update the seed for the next iteration
        self.seed = int(square_str[2:10])
        return number
    def generateNi(self):
        return self.min + (self.max - self.min) * self.middle_square()

# Ejemplo de uso:
ms = Middle_square(0, 100)
numero_generado = ms.middle_square()
print(numero_generado)
