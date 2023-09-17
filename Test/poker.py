import pandas as pd
import scipy.stats as stats

def truncar_a_5_digitos(numero):
    return round(numero, 5)

def contar_cantidad_categorias(numeros):
    categorias = {
        "par": 0,
        "dos_pares": 0,
        "trio": 0,
        "trio_y_par": 0,
        "poker": 0,
        "quintilla": 0,
        "aleatorio": 0
    }

    for numero in numeros:
        numero_truncado = truncar_a_5_digitos(numero)
        digitos = [int(d) for d in str(abs(numero_truncado)).replace('.', '')]
        conteo_digitos = {i: digitos.count(i) for i in digitos}

        if 5 in conteo_digitos.values():
            categorias["quintilla"] += 1
        elif 4 in conteo_digitos.values():
            categorias["poker"] += 1
        elif 3 in conteo_digitos.values():
            if 2 in conteo_digitos.values():
                categorias["trio_y_par"] += 1
            else:
                categorias["trio"] += 1
        elif 2 in conteo_digitos.values():
            if len(conteo_digitos) == 2:
                categorias["dos_pares"] += 1
            else:
                categorias["par"] += 1
        else:
            categorias["aleatorio"] += 1

    return categorias

# Example usage

numeros = [1.708585842,
0.3343438948,
0.9104974197,
0.1973000963,
1.702692316,
-0.04549406185,
0.1208934464,
-1.615208021,
-2.252472768,
-0.1090347723,
-0.1816454187,
-0.5452386631,
0.7814765013,
-0.5381525625,
0.2621891326,
-0.6301740996,
0.4062064818,
-0.1194302968,
-0.4284061106,
0.9084146768]


print(f"cantidad numeros: {len(numeros)}")
cantNum = len(numeros)

resultado = contar_cantidad_categorias(numeros)

# Create a DataFrame
tabla = pd.DataFrame({"Categoria": resultado.keys(), "Oi": resultado.values()})
# Add the "probabilidad" column
tabla["probabilidad"] = [0.504, 0.108, 0.072, 0.009, 0.0045, 0.0001, 0.3024]
tabla["Ei"] = tabla["probabilidad"] * cantNum
tabla["(Ei-Oi)^2/Ei"] = ((tabla["Ei"] - tabla["Oi"]) ** 2) / tabla["Ei"]

total = tabla["(Ei-Oi)^2/Ei"].sum()
print(tabla)

critical_value = stats.chi2.ppf(1 - 0.05, 6)

print (f"El total(Ei-Oi)^2/Ei es :  {total}")
print (f"Chi^2 : {critical_value}")

if(total < critical_value):
    print ("No se rechaza la hipotesis nula")
else:
    print ("Se rechaza la hipotesis nula")

