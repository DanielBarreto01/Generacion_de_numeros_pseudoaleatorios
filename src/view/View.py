import os
import tkinter as tk
from tkinter import ttk
from src.view.graph import Graph

class View:
    """def mostrar_mensaje(self, mensaje):
        print(f"Vista: {mensaje}")"""

    def __init__(self, presenter,lucky_archers,experienced_archers,winning_team,genders_by_game,gender_total_win,charr):
        self.charr= charr
        self.presenter = presenter
        self.root = tk.Tk()
        self.root.title("Montecarlo")
        self.root.configure(bg="black")
      #  self.archers_data = archers_data
        self.root.geometry("1280x720")
        self.root.resizable(False, False)


        #self.root.state('zoomed')
        #self.root.attributes('-fullscreen', False)  # full screen

        image_path = os.path.abspath("resources/9D.gif")
        self.image = tk.PhotoImage(file=image_path)

        desired_width = 475  # Ancho deseado
        current_width = self.image.width()
        scaling_factor = desired_width / current_width
        new_height = int(self.image.height() * scaling_factor)
        self.image = self.image.subsample(round(1 / scaling_factor), round(1 / scaling_factor))
        image_frame = tk.Frame(self.root, bg="black")
        image_frame.pack(side="top", fill="x")
        self.image_label = tk.Label(image_frame, image=self.image, bg="black")
        self.image_label.pack()

        left_frame = ttk.Frame(self.root, padding=2, width=200, height=300)
        left_frame.place(x=2, y=2)
        right_title_label = ttk.Label(left_frame, text="Most Lucky Archers", font=("Ebrima", 12, "bold"))
        right_title_label.pack(padx=10, pady=10, anchor="center")
        left_text = tk.Text(left_frame, wrap="word", width=38, height=20)
        left_text.pack(fill="both", expand=True, padx=10, pady=10)
        left_text.insert("1.0", lucky_archers)
        left_scrollbar = ttk.Scrollbar(left_frame, command=left_text.yview)
        left_scrollbar.pack(side="right", fill="y")
        left_text.config(yscrollcommand=left_scrollbar.set)

        left_frame = ttk.Frame(self.root, padding=2, width=200, height=300)
        left_frame.place(x=946, y=2)
        right_title_label = ttk.Label(left_frame, text="Most Experienced Archers", font=("Ebrima", 12, "bold"))
        right_title_label.pack(padx=10, pady=10, anchor="center")
        left_text = tk.Text(left_frame, wrap="word", width=38, height=20)
        left_text.pack(fill="both", expand=True, padx=10, pady=10)
        texto_prueba = experienced_archers
        left_text.insert("1.0", texto_prueba)
        left_scrollbar = ttk.Scrollbar(left_frame, command=left_text.yview)
        left_scrollbar.pack(side="right", fill="y")
        left_text.config(yscrollcommand=left_scrollbar.set)

        left_frame = ttk.Frame(self.root, padding=2, width=200, height=300)
        left_frame.place(x=2, y=450)
        right_title_label = ttk.Label(left_frame, text="Gender Victories", font=("Ebrima", 12, "bold"))
        right_title_label.pack(padx=10, pady=10, anchor="center")
        left_text = tk.Text(left_frame, wrap="word", width=80, height=9)
        left_text.pack(fill="both", expand=True, padx=10, pady=10)
        left_text.insert("1.0", genders_by_game)
        left_scrollbar = ttk.Scrollbar(left_frame, command=left_text.yview)
        left_scrollbar.pack(side="right", fill="y")
        left_text.config(yscrollcommand=left_scrollbar.set)

        left_frame = ttk.Frame(self.root, padding=2, width=200, height=300)
        left_frame.place(x=677, y=450)
        right_title_label = ttk.Label(left_frame, text="Winning Team", font=("Ebrima", 12, "bold"))
        right_title_label.pack(padx=10, pady=10, anchor="center")
        left_text = tk.Text(left_frame, wrap="word", width=74, height=1)
        left_text.pack(fill="both", expand=True, padx=10, pady=10)
        left_text.insert("1.0", winning_team)

        left_frame = ttk.Frame(self.root, padding=2, width=200, height=300)
        left_frame.place(x=677, y=545)
        right_title_label = ttk.Label(left_frame, text="Winning Gender", font=("Ebrima", 12, "bold"))
        right_title_label.pack(padx=10, pady=10, anchor="center")
        left_text = tk.Text(left_frame, wrap="word", width=74, height=1)
        left_text.pack(fill="both", expand=True, padx=10, pady=10)
        left_text.insert("1.0", gender_total_win)

        custom_button = tk.Button(self.root, text="Grafica", bg="light blue", width=85, height=4, command=self.button_click)
        custom_button.place(x=680, y=640)
        custom_button.pack_propagate(False)

        self.root.mainloop()

    def button_click(self):
        graph_window = Graph(self.root,self.charr)



    def run(self):
        self.root.mainloop()

    # Puedes definir métodos para manejar eventos de interfaz gráfica aquí

if __name__ == "__main__":
    view = View(None)
    view.run()