from src.models import *
from src.models import simulation
from src.view import View

class Controller:
    def __init__(self, game):
        print(game)
        self.simulation = simulation.Simulation(game)
        print(game)
        print(f"  {self.simulation.obtain_lucky_archers()}    {self.simulation.obtain_experienced_archers()}   {self.simulation.obtain_winning_team()}   {self.simulation.obtain_genders_by_game()}   {self.simulation.obtain_gender_total_win()}")
        #print(f"  {self.simulation.obtain_lucky_archers()} ")
        print("hola")
        self.vista = View.View()

    """def ejecutar(self):
        mensaje = self.modelo.obtener_mensaje()
        self.vista.mostrar_mensaje(mensaje)"""
