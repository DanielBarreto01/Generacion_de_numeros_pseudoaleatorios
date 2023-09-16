from middle_square import middle_square
from Gender import Gender
from Score import Score


import random

class Archer:
    def __init__(self, code):
        self.code = code
        self.generator = middle_square(0,1)
        self.experience = 10
        self.points = 0
        self.count_luck = 0
        self.score = None
        self.round_points = 0
        self.won_rounds = 0
        self.won_raffles = 0
        self.consecutive_won_raffle_number_round = -1
        self.initial_resistance = self.generate_resistance()
        self.resistance = self.initial_resistance
        self.luck = self.generate_luck()
        self.gender = self.generate_gender()

    #simula los lanzamientos de un aqruero
    def launch(self):
        launch = 0
        while self.resistance > 0:
            launch = self.individual_launch()
            self.points += launch
            self.round_points += launch
            self.resistance -= 5
        self.regain_resistance_round()
        self.regain_luck()

    #realiza lanzamiento segun el genero
    def individual_launch(self):
        return self.throwing_male() if self.gender == 'MALE' else self.throwing_female()

    #simula lanzamiento masculino 
    def throwing_male(self):
        random_val = self.generator.generateNi()
        if 0 < random_val <= 0.2:
            self.score = Score.CENTER
        elif 0.2 < random_val <= 0.53:
            self.score = Score.INTERMEDIATE
        elif 0.53 < random_val <= 0.93:
            self.score = Score.OUTSIDE
        elif 0.93 < random_val <= 1:
            self.score = Score.ERROR
        return self.score

    #simula lanzamiento femenio
    def throwing_female(self):
        random_val = self.generator.generateNi()
        if 0 < random_val <= 0.3:
            self.score = Score.CENTER
        elif 0.3 < random_val <= 0.68:
            self.score = Score.INTERMEDIATE
        elif 0.68 < random_val <= 0.95:
            self.score = Score.OUTSIDE
        elif 0.95 < random_val <= 1:
            self.score = Score.ERROR
        return self.score

    #aumenta el numero de rondas ganadas 
    def increase_won_rounds(self):
        self.won_rounds += 1

    #aumenta numero de lanzamoientos ganados consecutivo
    def increase_won_raffles(self, round_num):
        if self.consecutive_won_raffle_number_round == -1:
            self.consecutive_won_raffle_number_round = round_num
            self.won_raffles += 1
        elif self.consecutive_won_raffle_number_round + 1 == round_num:
            self.consecutive_won_raffle_number_round = round_num
            self.won_raffles += 1
        else:
            self.won_raffles = 1
            self.consecutive_won_raffle_number_round = round_num


    # genera genero aleatorio 
    def generate_gender(self):
        return Gender.MALE if self.generator.generateNi() >= 0.5 else Gender.FEMALE    # aleatorio iniforme 
    
    # Genera la suerte inicial
    def generate_luck(self):
        return self.self.generator.generateNi() * 2 + 1

    # Recupera la suerte del arquero                    # no le veo sentido
    def regain_luck(self):          
        self.luck = self.generate_luck()

        # Genera la resistencia inicial
    def generate_resistance(self):
        return int(self.self.generator.generateNi() * (45 - 25 + 1)) + 25
    
    # Recupera la resistencia despues de cada ronda  (como ajustar genera resistencia de cada ronda )
    def regain_resistance_round(self):
        self.resistance = self.initial_resistance - self.generate_fatigue()      # rraro ?
        self.initial_resistance = self.resistance

     #reduce reseistencia con base a experiencia
    def decrease_resistance_by_experience(self):
        self.resistance -= 1

    #recupera resistencia 
    def regain_resistance(self):
        self.resistance = self.initial_resistance

    #genera fatiga 
    def generate_fatigue(self):
        return int(self.generator.generateNi() * 2) + 1

    #aumenta la experiencia 
    def gain_experience(self):
        self.experience += 3


    #restablece puntos de ronda
    def regain_round_points(self):
        self.round_points = 0

    #aumenta la suerte 
    def increase_count_luck(self):
        self.count_luck += 1

    #restablece la suerte 
    def regain_count_luck(self):
        self.count_luck = 0

if __name__ == "__main__":
    archer = Archer(1)
    archer.launch()
    print("Archer Points:", archer.points)
    print("Archer Resistance:", archer.resistance)