import numpy as np
import pandas as pd
from scipy.stats import ksone
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import Label

class ks:
    def __init__(self, data):
        self.data = data
        
        

root = tk.Tk()
root.title("Tabla KS Test")

# Función para cargar un archivo CSV
data = [0.8294, 0.7904, 0.4732, 0.3918, 0.3507, 0.299, 0.9401, 0.3788, 0.3489, 0.1731]
# Ingresa tus valores de conjunto de datos

# Define el número de intervalos
num_intervals = 10


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

# Calcula la frecuencia acumulada
cumulative_frequency = np.cumsum(frequency)

# Calcula la frecuencia esperada acumulada (igual en una distribución uniforme)
expected_cumulative_frequency = [i * (n / num_intervals) for i in range(1, num_intervals + 1)]

# Calcula la probabilidad esperada acumulada (igual en una distribución uniforme)
expected_cumulative_probability = [(i / num_intervals) for i in range(1, num_intervals + 1)]

# Calcula la probabilidad obtenida acumulada
observed_cumulative_probability = [cf / n for cf in cumulative_frequency]

# Calcula la diferencia entre la probabilidad esperada y la probabilidad obtenida
difference_probability = [abs(ep - op) for ep, op in zip(expected_cumulative_probability, observed_cumulative_probability)]

d_max = np.max(np.abs(ecdf - [uniform_cdf(x, a, b) for x in sorted_data]))

def calcular_valores_criticos_ks(alpha, n):
    # Calcula el valor crítico KS
    valor_critico = ksone.ppf(1 - alpha / 2, n)
    
    return valor_critico



# Crea un DataFrame de Pandas para mostrar el procedimiento
data_table = pd.DataFrame({
    'No': list(range(1, num_intervals + 1)),
    'Inicial': [interval[0] for interval in intervals],
    'Final': [interval[1] for interval in intervals],
    'Frec Obt': frequency,
    'Frec.Obt.A': cumulative_frequency,
    'Prob Obtenida': observed_cumulative_probability,
    'Frec Esp A': expected_cumulative_frequency,
    'P Esp.A': expected_cumulative_probability,
    'Dif': difference_probability
})

# Formatea las columnas para mostrar 4 decimales
data_table['Prob Obtenida'] = data_table['Prob Obtenida'].round(4)
data_table['P Esp.A'] = data_table['P Esp.A'].round(4)
data_table['Dif'] = data_table['Dif'].round(4)

pd.set_option('display.max_columns', None)
# Muestra la tabla
print(data_table)

## Calcula el valor crítico KS
n = 10
alpha = 0.05
valor_critico = calcular_valores_criticos_ks(alpha, n)
print(f"Valor crítico KS para alpha={alpha} y n={n}: {valor_critico}")
print (f"DMAX: {d_max}")



if(d_max < valor_critico):
    print("No se rechaza la hipótesis nula")
else:
    print("Se rechaza la hipótesis nula")
    

# Crear un widget Treeview de Tkinter para mostrar la tabla
table = ttk.Treeview(root, columns=list(data_table.columns), show="headings")
table.column("No", width="50")
table.column("Inicial", width="130")
table.column("Final", width="130")
table.column("Frec Obt", width="70")
table.column("Frec.Obt.A", width="70")
table.column("Prob Obtenida", width="70")
table.column("Frec Esp A", width="70")
table.column("P Esp.A", width="70")
table.column("Dif", width="60")

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


critico_label = Label(root, text=f"Valor crítico KS para alpha={alpha} y n={n}: {valor_critico}")
critico_label.grid(row=3, column=0, padx=10, pady=10)

dmax_label = Label(root, text=f"DMAX: {d_max}")
dmax_label.grid(row=4, column=0, padx=10, pady=10)

if(d_max < valor_critico):
    veredicto_label = Label(root, text="No se rechaza la hipótesis nula")
else:
    veredicto_label = Label(root, text="Se rechaza la hipótesis nula")
    
veredicto_label.grid(row=5, column=0, padx=10, pady=10)



# Ejecutar la aplicación de Tkinter
root.mainloop()

if __name__ == "__main__":

    root = tk.Tk()
    app = ks(root, data)

