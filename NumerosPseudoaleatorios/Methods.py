import random
import numpy as np
import time

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

    def distribucion_normal(self,a,b,n):

        print("Distribución Normal")
        random_array = np.random.uniform(a, b, n)
        pass

        for i in range(n):
            print("{}.  {}".format(i, random_array[i]))
     
        #toma la fecha para genrar el numero pseudoaleatorio   
    def congruenciales(self,n):
        print("Congruenciales")
        xn = int(time.time())
        for i in range(n):
             xn1 = ((1103515245 * xn + 12345) % 32768) / 32768.00
             print(xn1)
             xn = xn1

methods_instance = Methods()



# Llamar al método cuadrados_medios a través de la instancia
methods_instance.cuadrados_medios("7543", 10)
methods_instance.distribucion_normal(0,1,10)
methods_instance.congruenciales(10)
