import tkinter as tk
import matplotlib.pyplot as plt
class Graph:
    def __init__(self, parent,arches):
        self.arches =arches
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.title("Grafica")
        print(len(arches))
        self.y1 = []
        self.y2 = []
        self.y3 = []
        self.y4 = []
        self.y5 = []
        self.y6 = []
        self.y7 = []
        self.y8 = []
        self.y9 = []
        self.y10 = []
        self.x = [i+1 for i in range(10)]
        self.pac()
        self.x1 = [i+1 for i in range(len(self.y1))]
        self.h()
        self.graph()

        popup_text = tk.Text(self.window, wrap="word")
        popup_text.pack(fill="both", expand=True, padx=10, pady=10)
        popup_text.insert("1.0", "GRAFICA ")

      #  popup_text.insert("1.0", archers_data)
        def pac(self):
            aux_archer = None
            for i in range(len(self.arches)):
                aux_archer = self.arches[i]
                match aux_archer.code:
                    case 1:
                        self.y1.append(aux_archer.get_points())
                    case 2:
                        self.y2.append( aux_archer.get_points())
                    case 3:
                        self.y3.append(aux_archer.get_points())
                    case 4:
                        self.y4.append( aux_archer.get_points())
                    case 5:
                        self.y5.append(aux_archer.get_points())
                    case 6:
                        self.y6.append(aux_archer.get_points())
                    case 7:
                        self.y7.append(aux_archer.get_points())
                    case 8:
                        self.y8.append(aux_archer.get_points())
                    case 9:
                        self.y9.append(aux_archer.get_points())
                    case 10:
                        self.y10.append(aux_archer.get_points())

            print(self.y1)
            print(self.x)
        def h(self):
            print(self.x1)

        def graph(self):
            plt.plot(self.x1, self.y1, label='Arquero 1')
            plt.plot(self.x1, self.y2, label='Arquero 2')
            plt.plot(self.x1, self.y3, label='Arquero 3')
            plt.plot(self.x1, self.y4, label='Arquero 4')
            plt.plot(self.x1, self.y5, label='Arquero 5')
            plt.plot(self.x1, self.y6, label='Arquero 6')
            plt.plot(self.x1, self.y7, label='Arquero 7')
            plt.plot(self.x1, self.y8, label='Arquero 8')
            plt.plot(self.x1, self.y9, label='Arquero 9')
            plt.plot(self.x1, self.y10, label='Arquero 10')

            # Agregar etiquetas a los ejes y título
            plt.xlabel('Game')
            plt.ylabel('Points')
            plt.title('Putntos Jugadores vs Juegos')

            # Mostrar una leyenda
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.09), fancybox=True, shadow=True, ncol=10, fontsize='small')

            # Mostrar la gráfica
            plt.show()