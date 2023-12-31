import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

class PseudoRandomValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validación de Números Pseudoaleatorios")

        # Crear y configurar la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Botón para cargar un archivo con números pseudoaleatorios
        self.load_button = tk.Button(self.root, text="Cargar Archivo", command=self.load_file)
        self.load_button.pack()

        # Lista desplegable para seleccionar la prueba a realizar
        self.test_label = tk.Label(self.root, text="Seleccione la prueba:")
        self.test_label.pack()

        self.test_options = ["Prueba de Medias", "Prueba de Varianza", "Prueba KS", "Prueba Chi2", "Prueba de Póker"]
        self.selected_test = tk.StringVar()
        self.test_dropdown = tk.OptionMenu(self.root, self.selected_test, *self.test_options)
        self.test_dropdown.pack()

        # Botón para realizar la prueba seleccionada
        self.run_test_button = tk.Button(self.root, text="Realizar Prueba", command=self.run_test)
        self.run_test_button.pack()

        # Gráfico para mostrar los resultados
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()

        # Tabla para mostrar los resultados de la prueba de medias
        self.result_table_mean = tk.Text(self.root, height=10, width=40)
        self.result_table_mean.pack()

        # Tabla para mostrar los resultados de la prueba de varianza
        self.result_table_variance = tk.Text(self.root, height=10, width=40)
        self.result_table_variance.pack()

    def load_file(self):
        # Abrir un cuadro de diálogo para seleccionar un archivo CSV
        file_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])

        # Leer los números pseudoaleatorios del archivo CSV usando pandas
        df = pd.read_csv(file_path)
        self.random_numbers = df['Numero'].tolist()  # Suponemos que el CSV tiene una columna llamada 'Numero'

        # Realizar la prueba de medias y mostrar los resultados en la tabla
        self.run_mean_test_and_display()

    def run_test(self):
        if not hasattr(self, 'random_numbers'):
            return

        selected_test = self.selected_test.get()

        if selected_test == "Prueba de Medias":
            self.run_mean_test_and_display()
        elif selected_test == "Prueba de Varianza":
            self.run_variance_test_and_display()
        # Resto de las pruebas aquí ...

    def run_mean_test_and_display(self):
        if not hasattr(self, 'random_numbers'):
            return

        # Realizar la prueba de medias
        mean = np.mean(self.random_numbers)
        result = f"Media: {mean:.4f}"

        # Mostrar el resultado en la tabla de medias
        self.result_table_mean.delete("1.0", "end")  # Borrar contenido anterior
        self.result_table_mean.insert("end", result)

        # Crear y mostrar la tabla con tres columnas: "Numero", "Ni", "Normalizados"
        table_data = []
        n = len(self.random_numbers)
        for i, num in enumerate(self.random_numbers):
            table_data.append([i + 1, num, i / n])

        table_headers = ["Numero", "Ni", "Normalizados"]
        table_df = pd.DataFrame(table_data, columns=table_headers)

        self.result_table_mean.insert("end", "\nTabla de Datos:\n")
        self.result_table_mean.insert("end", table_df.to_string(index=False))

        # Mostrar el banner con información de aceptación y alfa
        alpha = 0.05  # Cambia esto según  nivel de confianza
        self.result_table_mean.insert("end", f"\n\nNivel de confianza (alfa): {alpha}\n")
        self.result_table_mean.insert("end", "Resultado de Aceptación: ")

        if mean < (1 - alpha / 2) and mean > alpha / 2:
            self.result_table_mean.insert("end", "Aceptado")
        else:
            self.result_table_mean.insert("end", "Rechazado")

    def run_variance_test_and_display(self):
        if not hasattr(self, 'random_numbers'):
            return

        # Realizar la prueba de varianza
        variance = np.var(self.random_numbers)
        n = len(self.random_numbers)

        # Calcular los valores críticos para la prueba de varianza
        alpha = 0.05  # Nivel de confianza (puedes ajustarlo según tus necesidades)
        chi2_left = stats.chi2.ppf(alpha / 2, df=n - 1)
        chi2_right = stats.chi2.ppf(1 - alpha / 2, df=n - 1)

        result = f"Varianza: {variance:.4f}\nN: {n}\n"
        result += f"Chi2 izquierdo: {chi2_left:.4f}\nChi2 derecho: {chi2_right:.4f}\n"

        # Comprobar si la varianza es aceptada o rechazada
        if chi2_left <= (n - 1) * variance <= chi2_right:
            result += "Resultado: Aceptado"
        else:
            result += "Resultado: Rechazado"

        # Mostrar el resultado en la tabla de varianza
        self.result_table_variance.delete("1.0", "end")  # Borrar contenido anterior
        self.result_table_variance.insert("end", result)

    # Resto de los métodos de prueba aquí ...

    def plot_result(self, result):
        self.canvas.delete("all")
        self.canvas.create_text(200, 150, text=result, font=("Helvetica", 12), justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = PseudoRandomValidatorApp(root)
    root.mainloop()
