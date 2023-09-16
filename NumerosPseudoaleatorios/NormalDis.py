import tkinter as tk
from tkinter import ttk
import random
import Methods
from Models.middle_square import Middle_square
from Models.UniformDis import Uniform

class NormalDistributionGenerator:
    
        
    def __init__(self, root):
       # self.methodos_instacnce=Methods.Methods()
        
          # Calcula el ancho y alto de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

          # Calcula el ancho y alto de la pantalla
        window_width = 800  # Cambia esto al ancho deseado
        window_height = 700

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
        self.metodo_metod = ttk.Combobox(root, values=["Cuadrados Medios", "congruenciales", "Distribución Uniforme","distribución normal"])
    
        self.generate_button = ttk.Button(root, text="Generar", command=lambda: self.select_methods(self.metodo_metod.get()))


        # Crear tabla para mostrar los números
        self.table = ttk.Treeview(root, columns=("i","Ri", "Ni"))
        self.table.heading("#0", text="")
        self.table.heading("#1", text="i")
        self.table.heading("#2", text="Ri")
        self.table.heading("#3", text="Ni")
    

        self.table.column("#0", width=0, anchor="center")
        self.table.column("#1", width=280, anchor="center")
        self.table.column("#2", width=280, anchor="center")
        self.table.column("#3", width=300, anchor="center")
    

        # Centrar elementos verticalmente
        self.min_label.pack()
        self.min_entry.pack()
        self.max_label.pack()
        self.max_entry.pack()
        self.quantity_label.pack()
        self.quantity_entry.pack()
        self.metodo.pack()
        self.metodo_metod.pack()
        self.generate_button.pack()

        # Configurar la tabla
        self.table.pack()
        self.table["height"] = 16

        
        

    
    def paint_table(self,list_numbers):
        # Elimina las filas de la tabla
        for row in self.table.get_children():
            self.table.delete(row)

        for row in self.table.get_children():
            self.table.item(row, column=1, values="")
            self.table.item(row, column=2, values="")
            self.table.item(row, column=3, values="")

        valores_divididos = []
        for i, num in enumerate(list_numbers, start=1):
            valor_dividido = int(num) / 10000  # Divide el número por 10000
            valores_divididos.append(str(valor_dividido))

        # Mostrar los números en la tabla
        # Mostrar los números en la tabla
        for i, (num, valor_dividido) in enumerate(zip(list_numbers, valores_divididos), start=1):
            self.table.insert("", "end", values=(i,valor_dividido, num))

        print(list_numbers, "numeros semilla")
        print(valores_divididos, "valores divididos")



    def select_methods(self,method):
        min_value = int(self.min_entry.get())
        max_value = int(self.max_entry.get())
        quantity_value = int(self.quantity_entry.get())

        match method:
            case "Cuadrados Medios":
                self.middle_square_instance = Middle_square(min_value, max_value, quantity_value)
                n=self.middle_square_instance.middle_square()
                self.paint_table(n)
            case "Distribución Uniforme":
                self.uniform_instance = Uniform(quantity_value, min_value, max_value)
                self.uniform_instance.generate_random()
                self.paint_table(self.uniform_instance.aleatory)
                pass
            case _:
                print("Método no válido")

        
                print(min_value, max_value, quantity_value, method)
        print("entre selec metodos")
        
        


def main():
    root = tk.Tk()
    app = NormalDistributionGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
