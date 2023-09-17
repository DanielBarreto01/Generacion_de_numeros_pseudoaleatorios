import tkinter as tk
class Graph:
    def __init__(self, parent,):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Grafica")

        popup_text = tk.Text(self.window, wrap="word")
        popup_text.pack(fill="both", expand=True, padx=10, pady=10)
        popup_text.insert("1.0", "GRAFICA ")

        # Agrega  contenido

      #  popup_text.insert("1.0", archers_data)
