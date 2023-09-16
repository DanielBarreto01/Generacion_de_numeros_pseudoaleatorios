from scipy.stats import kstest

# Aquí, ingresa tus valores de conjunto de datos en lugar de generar números pseudoaleatorios.
# Reemplaza los valores en la lista "data" con tus propios datos.
data = [0.7512146762472678, 0.9530568573371749, 0.32062119846682857, 0.3132448347613781, 0.7215224880861777, 0.09882448903533514, 0.8790437005810573, 0.6208638808603902, 0.7280655477241308, 0.42416317216705257]

# Realiza el Test de Kolmogorov-Smirnov
# Aquí, especificamos la distribución con la que deseamos comparar nuestros datos,
# en este caso, una distribución uniforme.
ks_statistic, ks_p_value = kstest(data, 'uniform', args=(min(data), max(data)))

# Imprime los resultados
print("Estadística KS:", ks_statistic)
print("Valor p:", ks_p_value)

# Establece un nivel de significancia (alfa) para tu prueba
alfa = 0.05

# Compara el valor p con el nivel de significancia
if ks_p_value < alfa:
    print("Se rechaza la hipótesis nula: Los datos no siguen una distribución uniforme.")
else:
    print("No se puede rechazar la hipótesis nula: Los datos siguen una distribución uniforme.")
