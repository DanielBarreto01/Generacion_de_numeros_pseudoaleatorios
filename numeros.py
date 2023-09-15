import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from random import seed

class RandomNumberGeneratorApp:
    def __init__(self, root):
        
        self.root = root

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

        self.root.title("Generador de Números Pseudoaleatorios")
        
        self.method_label = ttk.Label(root, text="Método:")
        self.method_label.pack()
        
        self.method_var = tk.StringVar()
        self.method_combo = ttk.Combobox(root, textvariable=self.method_var, values=["Cuadrados Medios", "Congruencial Lineal"])
        self.method_combo.pack()
        
        self.generate_button = ttk.Button(root, text="Generar", command=self.generate_numbers)
        self.style.configure('TButton', background='#4CAF50', foreground='white')
        
        self.generate_button.pack() 
        
        self.result_label = ttk.Label(root, text="")
        self.result_label.pack()
        
        self.numbers = []

    def generate_cuadrados_medios(self):
        seed_value = int(input("Ingresa la semilla: "))
        numbers = []
        for _ in range(10):  # Generar 10 números pseudoaleatorios
            seed_value = int(str(seed_value ** 2).zfill(8)[2:6])
            numbers.append(seed_value / 10000)
        return numbers

    def generate_congruencial_lineal(self):
        m = 2**31 - 1
        a = 7**5
        c = 0
        seed_value = int(input("Ingresa la semilla: "))
        numbers = []
        for _ in range(10):  # Generar 10 números pseudoaleatorios
            seed_value = (a * seed_value + c) % m
            numbers.append(seed_value / m)
        return numbers
    
    def plot_numbers(self):
        if not self.numbers:
            return
        
        plt.plot(self.numbers, marker='o')
        plt.title("Números Pseudoaleatorios Generados")
        plt.xlabel("Iteración")
        plt.ylabel("Valor")
        plt.show()
    
    def generate_numbers(self):
        if self.method_var.get() == "Cuadrados Medios":
            self.numbers = self.generate_cuadrados_medios()
        elif self.method_var.get() == "Congruencial Lineal":
            self.numbers = self.generate_congruencial_lineal()
        
        self.result_label.config(text=f"Números generados: {', '.join(map(str, self.numbers))}")
        self.plot_numbers()

if __name__ == "__main__":
    root = tk.Tk()
    app = RandomNumberGeneratorApp(root)
    root.resizable(False, False)    
    root.configure(background="#CAF1EF")
    root.mainloop()
