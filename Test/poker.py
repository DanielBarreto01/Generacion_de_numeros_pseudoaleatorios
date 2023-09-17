import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import scipy.stats as stats
root = tk.Tk()
root.title("Tabla poker Test")

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

numeros = [1,2,87]


print(f"cantidad numeros: {len(numeros)}")
cantNum = len(numeros)

resultado = contar_cantidad_categorias(numeros)

# Create a DataFrame
tabla = pd.DataFrame({"Categoria": resultado.keys(), "Oi": resultado.values()})
# Add the "probabilidad" column
tabla["probabilidad"] = [0.504, 0.108, 0.072, 0.009, 0.0045, 0.0001, 0.3024]
##################################
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
    
table = ttk.Treeview(root, columns=list(tabla.columns), show="headings")
table.column("Categoria", width="100")
table.column("Oi", width="60")
table.column("probabilidad", width="100")
table.column("Ei", width="100")
table.column("(Ei-Oi)^2/Ei", width="150")

# Configurar encabezados de columnas
for col in tabla.columns:
    table.heading(col, text=col)

# Agregar filas de datos a la tabla
for i, row in tabla.iterrows():
    table.insert('', 'end', values=list(row))

# Colocar la tabla en la ventana
table.grid(row=0, column=0, padx=10, pady=10)


# Función para cerrar la ventana cuando se haga clic en el botón de "Cerrar"
def cerrar_ventana():
    root.destroy()

# Botón para cerrar la ventana
boton_cerrar = ttk.Button(root, text="Cerrar", command=cerrar_ventana)
boton_cerrar.grid(row=1, column=0, padx=10, pady=10)

resultado_label = tk.Label(root, text=f"El total(Ei-Oi)^2/Ei es :  {total}")
resultado_label.grid(row=2, column=0, padx=10, pady=10)

chi2_label = tk.Label(root, text=f"Chi^2 : {critical_value}")
chi2_label.grid(row=3, column=0, padx=10, pady=10)

if(total < critical_value):
    veredicto_label = tk.Label(root, text="No se rechaza la hipótesis nula")
else:
    veredicto_label = tk.Label(root, text="Se rechaza la hipótesis nula")
    
veredicto_label.grid(row=4, column=0, padx=10, pady=10)

# Ejecutar la aplicación de Tkinter
root.mainloop()