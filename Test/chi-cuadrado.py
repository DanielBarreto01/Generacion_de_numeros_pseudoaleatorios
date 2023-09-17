import numpy as np
import pandas as pd
from scipy.stats import ksone
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
import tkinter as tk
from tkinter import ttk
from tkinter import Label
# Ingresa tus valores de conjunto de datos
data = [0.9634731371579395, 0.8846470279646376, 0.7266874660722045, 0.35868355450366385, 0.3402934242066663, 0.2699767328916134, 0.31722243341888456, 0.5614001017785968, 0.8342195117324919, 0.7615286765340064]
total_datos = data.__len__()
#El numero de intervalos es igual a la raiz cuadrada del numero de datos
m = math.sqrt(total_datos)
num_intervals = round(m)

root = tk.Tk()
root.title("Tabla Chi Cuadrado")

#Ei = numero elementos / numero intervalos
ei = total_datos / num_intervals

# Ordena los datos
sorted_data = np.sort(data)

# Calcula la ECDF
n = len(sorted_data)
ecdf = np.arange(1, n + 1) / n

# Define la función de distribución acumulada (CDF) teórica (ejemplo para distribución uniforme)
def uniform_cdf(x, a, b):
    if x < a:
        return 0
    elif x >= b:
        return 1
    else:
        return (x - a) / (b - a)

# Calcula la diferencia máxima entre la ECDF y la CDF teórica
a = min(data)
b = max(data)

d_max = np.max(np.abs(ecdf - [uniform_cdf(x, a, b) for x in sorted_data]))

# Divide el rango de datos en intervalos
interval_width = (b - a) / num_intervals
intervals = [(a + i * interval_width, a + (i + 1) * interval_width) for i in range(num_intervals)]

# Calcula la frecuencia de cada número en el intervalo
frequency = []
for interval in intervals:
    count = len([x for x in sorted_data if interval[0] <= x < interval[1]])
    frequency.append(count)
    
# Calcula la expresión (Ei - Oi)^2 / Ei
squared_difference = [((ei - observed) ** 2) / ei for observed in frequency]
    

data_table = pd.DataFrame({
    'Int': list(range(1, num_intervals + 1)),
    'Inicial': [interval[0] for interval in intervals],
    'Final': [interval[1] for interval in intervals],
    'Oi': frequency,
    'Ei': [ei] * num_intervals,
    '(Ei-Oi)^2/Ei': squared_difference
})

print(data_table)

#Suma toda la columna "Ei-Oi)^2/Ei"
total = data_table["(Ei-Oi)^2/Ei"].sum()
print (f"El total(Ei-Oi)^2/Ei es :  {total}")

critical_value = stats.chi2.ppf(1 - 0.05, num_intervals - 1)
print (f"Chi^2 : {critical_value}")

if(total < critical_value):
    print ("No se rechaza la hipotesis nula")
else:
    print ("Se rechaza la hipotesis nula")

table = ttk.Treeview(root, columns=list(data_table.columns), show="headings")
table.column("Int", width="50")
table.column("Inicial", width="100")
table.column("Final", width="100")
table.column("Oi", width="60")
table.column("Ei", width="100")
table.column("(Ei-Oi)^2/Ei", width="150")

# Configurar encabezados de columnas
for col in data_table.columns:
    table.heading(col, text=col)

# Agregar filas de datos a la tabla
for i, row in data_table.iterrows():
    table.insert('', 'end', values=list(row))

# Colocar la tabla en la ventana
table.grid(row=0, column=0, padx=10, pady=10)



# Función para cerrar la ventana cuando se haga clic en el botón de "Cerrar"
def cerrar_ventana():
    root.destroy()

# Botón para cerrar la ventana
boton_cerrar = ttk.Button(root, text="Cerrar", command=cerrar_ventana)
boton_cerrar.grid(row=1, column=0, padx=10, pady=10)

# Después de crear la tabla y antes de configurar el botón "Cerrar"

# Etiqueta para mostrar el resultado de (Ei-Oi)^2/Ei
resultado_label = Label(root, text=f"El total(Ei-Oi)^2/Ei es :  {total}")
resultado_label.grid(row=2, column=0, padx=10, pady=10)

# Etiqueta para mostrar el valor de Chi^2
chi2_label = Label(root, text=f"Chi^2 : {critical_value}")
chi2_label.grid(row=3, column=0, padx=10, pady=10)

# Etiqueta para mostrar si se rechaza o no la hipótesis nula
if total < critical_value:
    veredicto_label = Label(root, text="No se rechaza la hipotesis nula")
else:
    veredicto_label = Label(root, text="Se rechaza la hipotesis nula")

veredicto_label.grid(row=4, column=0, padx=10, pady=10)


# Ejecutar la aplicación de Tkinter
root.mainloop()