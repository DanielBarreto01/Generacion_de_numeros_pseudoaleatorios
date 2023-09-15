import tkinter as tk
from tkinter import ttk
import random

class NormalDistributionGenerator:
    def __init__(self, root):
          # Calcula el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

          # Calcula el ancho y alto de la pantalla
        window_width = 800  # Cambia esto al ancho deseado
        window_height = 600

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configura la geometría de la ventana
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root = root
        self.root.title("Generador de Distribución Normal")

        # Crear etiquetas y campos de entrada
        self.min_label = ttk.Label(root, text="Número Mínimo:")
        self.min_entry = ttk.Entry(root)
        self.max_label = ttk.Label(root, text="Número Máximo:")
        self.max_entry = ttk.Entry(root)
        self.quantity_label = ttk.Label(root, text="Cantidad de Números:")
        self.quantity_entry = ttk.Entry(root)

        self.metodo = ttk.Label(root, text="Metodo de Generacion")
        self.metodo_metod = ttk.Combobox(root, values=["Cuadrados Medios", "congruenciales", "distribución uniforme","distribución normal"])
        self.metodo_metod.set("Cuadrados Medios")
        self.generate_button = ttk.Button(root, text="Generar", command=self.generate_random_numbers)

        # Crear tabla para mostrar los números
        self.table = ttk.Treeview(root, columns=("i", "Ri", "Ni"))
        self.table.heading("#1", text="i")
        self.table.heading("#2", text="Ri")
        self.table.heading("#3", text="Ni")

        # Posicionar elementos en la interfaz
        self.min_label.grid(row=0, column=0)
        self.min_entry.grid(row=0, column=1)
        self.max_label.grid(row=1, column=0)
        self.max_entry.grid(row=1, column=1)
        self.metodo.grid(row=3, column=0)
        self.quantity_label.grid(row=2, column=0)
        self.quantity_entry.grid(row=2, column=1)
        self.metodo_metod.grid(row=3, column=1)
        self.generate_button.grid(row=4, columnspan=4)
        self.table.grid(row=6, columnspan=4)

    def generate_random_numbers(self):
        # Obtener valores ingresados por el usuario
        min_value = float(self.min_entry.get())
        max_value = float(self.max_entry.get())
        quantity = int(self.quantity_entry.get())

        # Generar números aleatorios en el rango especificado
        random_numbers = [round(random.uniform(min_value, max_value), 2) for _ in range(quantity)]

        # Limpiar la tabla antes de agregar nuevos datos
        for row in self.table.get_children():
            self.table.delete(row)

        # Mostrar los números en la tabla
        for num in random_numbers:
            self.table.insert("", "end", values=(num,))

def main():
    root = tk.Tk()
    app = NormalDistributionGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
