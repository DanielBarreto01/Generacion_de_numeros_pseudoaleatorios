import tkinter as tk
from tkinter import ttk
import random
from Models.middle_square import Middle_square
from Models.UniformDis import Uniform
from Models.Multiplicative import Multiplicative
from Models.NormalDistribution import NormalDistribution

class Run:
    
        
    def __init__(self, root):
       # self.methodos_instacnce=Methods.Methods()
        
          # Calcula el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

          # Calcula el ancho y alto de la pantalla
        window_width = 850  # Cambia esto al ancho deseado
        window_height = 700 # Cambia esto al alto deseado

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Configura la geometría de la ventana
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root = root
        self.root.title("Generador de Distribución Normal")
        self.root.resizable(False, False)

        # Crear etiquetas y campos de entrada
        self.min_label = ttk.Label(root, text="Número Mínimo:")
        self.min_entry = ttk.Entry(root)
        self.max_label = ttk.Label(root, text="Número Máximo:")
        self.max_entry = ttk.Entry(root)
        self.quantity_label = ttk.Label(root, text="Cantidad de Números:")
        self.quantity_entry = ttk.Entry(root)

        self.x_label = ttk.Label(root, text="Valor de X:")
        self.x_entry = ttk.Entry(root)
        self.t_label = ttk.Label(root, text="Valor de t:")
        self.t_entry = ttk.Entry(root)
        self.g_label = ttk.Label(root, text="Valor de g:")
        self.g_entry = ttk.Entry(root)

        self.metodo = ttk.Label(root, text="Metodo de Generacion")
        self.metodo_metod = ttk.Combobox(root, values=["Cuadrados Medios", "Multiplicativo", "Distribución Uniforme","Distribución Normal"])
    
        self.generate_button = ttk.Button(root, text="Generar", command=lambda: self.select_methods(self.metodo_metod.get()))

        self.table = ttk.Treeview(root, columns=("Xi", "Ri", "Ni"))
        self.table.heading("#0", text="")
        self.table.heading("#1", text="Xi")
        self.table.heading("#2", text="Ri")
        self.table.heading("#3", text="Ni")
    
        self.table.column("#0", width=0, anchor="center")
        self.table.column("#1", width=265, anchor="center")
        self.table.column("#2", width=265, anchor="center")
        self.table.column("#3", width=270, anchor="center")

        self.center_elements()

    def center_elements(self):
        # Centrar todos los elementos en la ventana
        self.min_label.grid(row=0, column=0, padx=2, pady=4, sticky="e")
        self.min_entry.grid(row=0, column=1, padx=2, pady=4, sticky="w")

        self.max_label.grid(row=1, column=0, padx=2, pady=5, sticky="e")
        self.max_entry.grid(row=1, column=1, padx=2, pady=5, sticky="w")

        self.quantity_label.grid(row=2, column=0, padx=2, pady=5, sticky="e")
        self.quantity_entry.grid(row=2, column=1, padx=2, pady=5, sticky="w")

        # Para las etiquetas y campos adicionales, sigue el mismo patrón
        self.x_label.grid(row=3, column=0, padx=2, pady=5, sticky="e")
        self.x_entry.grid(row=3, column=1, padx=2, pady=5, sticky="w")

        self.t_label.grid(row=4, column=0, padx=2, pady=5, sticky="e")
        self.t_entry.grid(row=4, column=1, padx=2, pady=5, sticky="w")

        self.g_label.grid(row=5, column=0, padx=2, pady=5, sticky="e")
        self.g_entry.grid(row=5, column=1, padx=2, pady=5, sticky="w")

        self.metodo.grid(row=6, column=0, padx=2, pady=5, sticky="e")
        self.metodo_metod.grid(row=6, column=1, padx=2, pady=5, sticky="w")

        self.generate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.table.grid(row=8, column=0, columnspan=2, padx=20, pady=5, sticky="nsew")

        
        
    
    def paint_table(self,Xi,Ri,Ni):
        # Elimina las filas de la tabla
        for row in self.table.get_children():
            self.table.delete(row)

        for row in self.table.get_children():
            self.table.item(row, column=1, values="")
            self.table.item(row, column=2, values="")
            self.table.item(row, column=3, values="")

        # Mostrar los números en la tabla
        # Mostrar los números en la tabla
        for i, (Ni, Ri,Xi) in enumerate(zip(Ni, Ri,Xi), start=1):
            formatted_ri = f'{Ri:.10f}'
            self.table.insert("", "end", values=(Xi,formatted_ri, Ni))


    def select_methods(self,method):
        min_value = int(self.min_entry.get())
        max_value = int(self.max_entry.get())
        quantity_value = int(self.quantity_entry.get())

        match method:
            case "Cuadrados Medios":
                self.middle_square_instance = Middle_square(min_value, max_value, quantity_value)
                ni=self.middle_square_instance.middle_square()
                self.paint_table(self.middle_square_instance.getXi(),self.middle_square_instance.getRi(),ni)
            case "Distribución Uniforme":
                self.uniform_instance = Uniform(quantity_value, min_value, max_value)
                self.uniform_instance.generate_random()
                self.paint_table(self.uniform_instance.get_aleatory(),self.uniform_instance.getrRi(),self.uniform_instance.ni_sequence)
            case "Multiplicativo":
                x=int(self.x_entry.get())
                t=int(self.t_entry.get())
                g=int(self.g_entry.get())
                self.multiplicative_instance = Multiplicative(x, t, g, quantity_value)
                n=self.multiplicative_instance.get_aleatory()
                self.paint_table(n)
            case "Distribución Normal":
                self.normal_distribution_instance = NormalDistribution(min_value, max_value, quantity_value)
                self.normal_distribution_instance.generate_random()
                self.paint_table(self.normal_distribution_instance.get_aleatory(),self.normal_distribution_instance.getRi(),self.normal_distribution_instance.getNi())
                pass
            case _:
                print("Método no válido")

        
                print(min_value, max_value, quantity_value, method)
        print("entre selec metodos")
        
def main():
    root = tk.Tk()
    app = Run(root)
    root.mainloop()

if __name__ == "__main__":
    main()
