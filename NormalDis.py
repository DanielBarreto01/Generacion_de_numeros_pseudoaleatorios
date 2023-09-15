import tkinter as tk
from tkinter import ttk
import random

class NormalDistributionGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Distribución Normal")

        # Crear etiquetas y campos de entrada
        self.min_label = ttk.Label(root, text="Número Mínimo:")
        self.min_entry = ttk.Entry(root)
        self.max_label = ttk.Label(root, text="Número Máximo:")
        self.max_entry = ttk.Entry(root)
        self.quantity_label = ttk.Label(root, text="Cantidad de Números:")
        self.quantity_entry = ttk.Entry(root)

        # Botón para generar números aleatorios
        self.generate_button = ttk.Button(root, text="Generar", command=self.generate_random_numbers)

        # Crear tabla para mostrar los números
        self.table = ttk.Treeview(root, columns=("Número Aleatorio"))
        self.table.heading("#1", text="Número Aleatorio")

        # Posicionar elementos en la interfaz
        self.min_label.grid(row=0, column=0)
        self.min_entry.grid(row=0, column=1)
        self.max_label.grid(row=1, column=0)
        self.max_entry.grid(row=1, column=1)
        self.quantity_label.grid(row=2, column=0)
        self.quantity_entry.grid(row=2, column=1)
        self.generate_button.grid(row=3, columnspan=2)
        self.table.grid(row=4, columnspan=2)

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
