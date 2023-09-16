from model.Model import Model
from view.View import View

class Controller:
    def __init__(self):
        self.modelo = Model()
        self.vista = View()

    def ejecutar(self):
        mensaje = self.modelo.obtener_mensaje()
        self.vista.mostrar_mensaje(mensaje)
