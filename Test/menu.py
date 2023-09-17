import tkinter as tk
from tkinter import filedialog
import pandas as pd
# No importes la clase ks globalmente aquí

class GuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejecutar KS")
        
        self.label = tk.Label(root, text="Seleccione una prueba:")
        self.label.pack()
        
        self.var = tk.StringVar()
        self.combo = tk.OptionMenu(root, self.var, "chi", "ks", "poker")
        self.combo.pack()
        
        self.load_button = tk.Button(root, text="Cargar CSV", command=self.load_csv)
        self.load_button.pack()
        
        self.go_button = tk.Button(root, text="GO!", command=self.run_ks)
        self.go_button.pack()
        
        self.csv_data = None

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.csv_data = pd.read_csv(file_path)
            print("CSV cargado correctamente.")

    def run_ks(self):
        if self.csv_data is None:
            print("Por favor, cargue un archivo CSV primero.")
            return
        
        selected_test = self.var.get()
        
        if selected_test == "ks":
            from ks import ks  # Importa la clase ks dentro de la función run_ks
            ks_instance = ks(self.csv_data)  # Crea una instancia de la clase ks con los datos CSV


if __name__ == "__main__":
    root = tk.Tk()
    app = GuiApp(root)
    root.mainloop()
