import random
import numpy as np
import time

class Methods:
   

    def __init__(self):
        self.numeros = []    

    def cuadrados_medios(self,iteraciones):
        tam1 = len(str(7435))
        print(iteraciones)
        print("Cantidad de dígitos: ", tam1)
        iteraciones = int(iteraciones) 
        numero1 = int(time.time())
        for i in range(iteraciones):
                numero2 = numero1**2
                snumero2 = str(numero2)
                tam2 = len(snumero2)
                primerc = int((tam2 - tam1) / 2)
                self.numeros.append(snumero2[primerc:primerc+tam1])
                print(self.numeros, "   eueu")
               # print("{}.  {}".format(i, self.numeros))
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


Methods().cuadrados_medios(10)