import tkinter as tk
from tkinter import filedialog
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

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

    def load_file(self):
        # Abrir un cuadro de diálogo para seleccionar un archivo
        file_path = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

        # Leer los números pseudoaleatorios del archivo (suponemos un número por línea)
        with open(file_path, 'r') as file:
            self.random_numbers = [float(line.strip()) for line in file]

    def run_test(self):
        if not hasattr(self, 'random_numbers'):
            return

        selected_test = self.selected_test.get()

        if selected_test == "Prueba de Medias":
            result = self.run_mean_test()
        elif selected_test == "Prueba de Varianza":
            result = self.run_variance_test()
        elif selected_test == "Prueba KS":
            result = self.run_ks_test()
        elif selected_test == "Prueba Chi2":
            result = self.run_chi2_test()
        elif selected_test == "Prueba de Póker":
            result = self.run_poker_test()

        # Mostrar el resultado en el gráfico
        self.plot_result(result)

    def run_mean_test(self):
        # Realizar la prueba de medias
        mean = np.mean(self.random_numbers)
        return f"Media: {mean:.4f}"

    def run_variance_test(self):
        # Realizar la prueba de varianza
        variance = np.var(self.random_numbers)
        return f"Varianza: {variance:.4f}"

    def run_ks_test(self):
        # Realizar la prueba KS
        _, p_value = stats.kstest(self.random_numbers, 'uniform')
        return f"Valor p: {p_value:.4f}"

    def run_chi2_test(self):
        # Realizar la prueba Chi2
        _, p_value = stats.chisquare(self.random_numbers)
        return f"Valor p: {p_value:.4f}"

    def run_poker_test(self):
        # Realizar la prueba de Póker
        #  implementar lógica para la prueba de Póker
        return "Prueba de Póker no implementada"

    def plot_result(self, result):
        self.canvas.delete("all")
        self.canvas.create_text(200, 150, text=result, font=("Helvetica", 12), justify="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = PseudoRandomValidatorApp(root)
    root.mainloop()