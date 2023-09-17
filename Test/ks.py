import numpy as np
import pandas as pd
from scipy.stats import ksone
import matplotlib.pyplot as plt

# Ingresa tus valores de conjunto de datos
data = [0.9634731371579395, 0.8846470279646376, 0.7266874660722045, 0.35868355450366385, 0.3402934242066663, 0.2699767328916134, 0.31722243341888456, 0.5614001017785968, 0.8342195117324919, 0.7615286765340064]

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
    'Int': list(range(1, num_intervals + 1)),
    'Inicio del Intervalo': [interval[0] for interval in intervals],
    'Fin del Intervalo': [interval[1] for interval in intervals],
    'Frecuencia Observada': frequency,
    'Frecuencia Acumulada': cumulative_frequency,
    'Probabilidad Obtenida Acumulada': observed_cumulative_probability,
    'Frecuencia Esperada Acumulada': expected_cumulative_frequency,
    'Probabilidad Esperada Acumulada': expected_cumulative_probability,
    'Diferencia Probabilidad': difference_probability
})

# Formatea las columnas para mostrar 4 decimales
data_table['Probabilidad Obtenida Acumulada'] = data_table['Probabilidad Obtenida Acumulada'].round(4)
data_table['Probabilidad Esperada Acumulada'] = data_table['Probabilidad Esperada Acumulada'].round(4)
data_table['Diferencia Probabilidad'] = data_table['Diferencia Probabilidad'].round(4)

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
    
# Crea una figura y un eje
fig, ax = plt.subplots(figsize=(20, 12))

# Oculta los ejes
ax.axis('off')

# Muestra la tabla como una tabla de texto en la figura
ax.table(cellText=data_table.values, colLabels=data_table.columns, cellLoc='center', loc='center')

# Guarda la figura como una imagen
plt.savefig('tabla_resultados.png', bbox_inches='tight', pad_inches=0.1)    
    
    