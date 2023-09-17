from src.models import *
from src.view import View

class Controller:
    def __init__(self, game):
        self.simulation = self.simulation(game)
        print(f"  {self.simulation.obtain_lucky_archers()}    {self.simulation.obtain_experienced_archers()}   {self.simulation.obtain_winning_team()}")
        self.vista = View()

    """def ejecutar(self):
        mensaje = self.modelo.obtener_mensaje()
        self.vista.mostrar_mensaje(mensaje)"""
