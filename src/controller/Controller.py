from src.models import *
from src.models import simulation
from src.view.View import View

class Controller:
    def __init__(self, game):
        self.simulation = simulation.Simulation(game)
        #self.archers_data = self.simulation.get_archers_per_game()

        self.view = View(self,self.simulation.obtain_lucky_archers(),self.simulation.obtain_experienced_archers(),self.simulation.obtain_winning_team(),
                         self.simulation.obtain_genders_by_game(),self.simulation.obtain_gender_total_win(),self.simulation.get_archers_per_game())

