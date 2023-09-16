from src.models import middle_square
from src.models.Gender import Gender


class Archer:
    def __init__(self, codigo):
        self.generator = middle_square.Middle_square(0 ,1)
        self.code = codigo;
        self.gender = self.generate_gender()
        self.initial_resistance = self.generate_resistance()
        self.resistance = self.initial_resistance
        self.experience = 10;
        self.luck = self.generate_luck()
        self.points = 0
        self.roundPoints = 0
        self.wonRounds = 0
        self.wonRaffles = 0
        self.consecutive_won_raflle_number_round = -1
        self.countLuck = 0

    def get_code(self):
        return self.code

    def get_gender(self):
        return self.gender

    def get_resistance(self):
        return self.resistance

    def get_experience(self):
        return self.experience

    def get_luck(self):
        return self.luck

    def get_points(self):
        return self.points

    def get_won_rounds(self):
        return self.won_rounds

    def get_won_raffles(self):
        return self.won_raffles

    def get_round_points(self):
        return self.round_points

    def get_count_luck(self):
        return self.count_luck

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
        score = 0
        random_val = self.generator.uniform(0, 1)
        if 0 < random_val <= 0.2:
            score = Shoot.CENTRAL.get_score()
        elif 0.2 < random_val <= 0.53:
            score = Shoot.INTERMEDIATE.get_score()
        elif 0.53 < random_val <= 0.93:
            score = Shoot.OUTSIDE.get_score()
        elif 0.93 < random_val <= 1:
            score = Shoot.ERROR.get_score()
        return score

    def throwing_female(self):
        score = 0
        random_val = self.generator.uniform(0, 1)
        if 0 < random_val <= 0.3:
            score = Shoot.CENTRAL.get_score()
        elif 0.3 < random_val <= 0.68:
            score = Shoot.INTERMEDIATE.get_score()
        elif 0.68 < random_val <= 0.95:
            score = Shoot.OUTSIDE.get_score()
        elif 0.95 < random_val <= 1:
            score = Shoot.ERROR.get_score()
        return score

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
        return 'MALE' if self.generator.generateNi() >= 0.5 else 'FEMALE'

    def generate_resistance(self):
        return int(self.generator.generateNi() * (45 - 25 + 1)) + 25

    def generate_luck(self):
        return self.generator.generateNi() * 2 + 1

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

