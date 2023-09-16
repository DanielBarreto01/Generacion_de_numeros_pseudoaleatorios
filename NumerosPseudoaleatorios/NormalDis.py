import tkinter as tk
from tkinter import ttk
import random
import Methods

class NormalDistributionGenerator:
    
        
    def __init__(self, root):
        self.methodos_instacnce=Methods.Methods()
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
    
        self.generate_button = ttk.Button(root, text="Generar", command=lambda: self.select_methods(self.metodo_metod.get()))


        # Crear tabla para mostrar los números
        self.table = ttk.Treeview(root, columns=("i", "Ri", "Ni"))
        self.table.heading("#0", text="i")
        self.table.heading("#1", text="Ri")
        self.table.heading("#2", text="Ni")

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

        

    def paint_table(self):
        # Elimina las filas de la tabla
        for row in self.table.get_children():
            self.table.delete(row)

        for row in self.table.get_children():
            self.table.item(row, column=1, values="")
        # Mostrar los números en la tabla
        for i, num in enumerate(self.methodos_instacnce.numeros, start=1):
            self.table.insert("", "end", values=(i,"", num))
        print(self.methodos_instacnce.numeros)


    def select_methods(self,method):
        print("entre")
        if method == "Cuadrados Medios":
            self.methodos_instacnce.cuadrados_medios(self.quantity_entry.get())
            self.paint_table()
        else:
            print("No se ha seleccionado un método")
        """elif method == "congruenciales":
            self.congruenciales()
        elif method == "distribución uniforme":
            self.distribucion_uniforme()
        elif method == "distribución normal":
            self.distribucion_normal()"""
        
        


def main():
    root = tk.Tk()
    app = NormalDistributionGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
