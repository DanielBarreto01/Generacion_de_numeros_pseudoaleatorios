from middle_square import middle_square
from Gender import Gender
from Score import Score

import random

class Archer:
    def __init__(self, code):
        self.code = code
        self.generator = random.Random()
        self.gender = self.generate_gender()
        self.initial_resistance = self.generate_resistance()
        self.resistance = self.initial_resistance
        self.experience = 10
        self.luck = self.generate_luck()
        self.points = 0
        self.round_points = 0
        self.won_rounds = 0
        self.won_raffles = 0
        self.consecutive_won_raffle_number_round = -1
        self.count_luck = 0
        self.score = None

    def launch(self):
        launch = 0
        while self.resistance > 0:
            launch = self.individual_launch()
            self.points += launch
            self.round_points += launch
            self.resistance -= 5
        self.regain_resistance_round()
        self.regain_luck()

    def individual_launch(self):
        return self.throwing_male() if self.gender == 'MALE' else self.throwing_female()

    def throwing_male(self):
        random_val = self.generator.uniform(0, 1)
        if 0 < random_val <= 0.2:
            self.score = Score.CENTER
        elif 0.2 < random_val <= 0.53:
            self.score = Score.INTERMEDIATE
        elif 0.53 < random_val <= 0.93:
            self.score = Score.OUTSIDE
        elif 0.93 < random_val <= 1:
            self.score = Score.ERROR
        return self.score

    def throwing_female(self):
        random_val = self.generator.uniform(0, 1)
        if 0 < random_val <= 0.3:
            self.score = Score.CENTER
        elif 0.3 < random_val <= 0.68:
            self.score = Score.INTERMEDIATE
        elif 0.68 < random_val <= 0.95:
            self.score = Score.OUTSIDE
        elif 0.95 < random_val <= 1:
            self.score = Score.ERROR
        return self.score

    def increase_won_rounds(self):
        self.won_rounds += 1

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

    def generate_gender(self):
        return 'MALE' if self.generator.uniform(0, 1) >= 0.5 else 'FEMALE'

    def generate_resistance(self):
        return int(self.generator.uniform(0, 1) * (45 - 25 + 1)) + 25

    def generate_luck(self):
        return self.generator.uniform(0, 1) * 2 + 1

    def regain_luck(self):
        self.luck = self.generate_luck()

    def regain_resistance_round(self):
        self.resistance = self.initial_resistance - self.generate_fatigue()
        self.initial_resistance = self.resistance

    def regain_resistance(self):
        self.resistance = self.initial_resistance

    def generate_fatigue(self):
        return int(self.generator.uniform(0, 1) * 2) + 1

    def gain_experience(self):
        self.experience += 3

    def decrease_resistance_by_experience(self):
        self.resistance -= 1

    def regain_round_points(self):
        self.round_points = 0

    def increase_count_luck(self):
        self.count_luck += 1

    def regain_count_luck(self):
        self.count_luck = 0

if __name__ == "__main__":
    archer = Archer(1)
    archer.launch()
    print("Archer Points:", archer.points)
    print("Archer Resistance:", archer.resistance)