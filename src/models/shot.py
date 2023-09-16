from src.model import middle_square
from src.model.Gender import Gender


class Shot:
    def __init__(self, codigo):
        self.generator = middle_square(0, 1);
        self.this.code = codigo;
        self.gender = self.generate_gender();
        self.initial_resistance = self.generate_resistance();
        self.resistance = self.initial_resistance;
        self.experience = 10;
        self.luck = self.generateLuck();
        self.points = 0;
        self.roundPoints = 0;
        self.wonRounds = 0;
        self.wonRaffles = 0;
        self.consecutive_won_raflle_number_round = -1;
        self.countLuck = 0;

    def generate_gender(self):
        return Gender.MALE if self.generator.generateNi() >= 0.5 else Gender.FEMALE



