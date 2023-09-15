class Methods:

    def cuadrados_medios(self, semilla, iteraciones):
        numeros = []
        tam1 = len(semilla)
        print("Cantidad de dígitos: ", tam1)
        numero1 = int(semilla)
        for i in range(10):
                numero2 = numero1**2
                snumero2 = str(numero2)
                tam2 = len(snumero2)
                primerc = int((tam2 - tam1) / 2)
                numeros = snumero2[primerc:primerc+tam1]
                print("{}.  {}".format(i, numeros))
                numero1 = int(numeros)
# Crear una instancia de la clase Methods
methods_instance = Methods()

# Llamar al método cuadrados_medios a través de la instancia
methods_instance.cuadrados_medios("7543", 10)
