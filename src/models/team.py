from src.models import shot


class Team:
    def __init__(self, arches, code):
        # self.arches[0] = shot.Shot(5).
        self.arches = arches
        self.code = code
        self.score=0
        self.won_rounds = 0
        self.count_luck = 0

    def get_lucky_archer(self):
        lucky_archer = None
        max_lucky = 0
        for i in self.arches:
            if i.get_luck() > max_lucky:
                max_lucky = i.get_luck()
                lucky_archer = i
        return lucky_archer

    def increase_luck_to_archer(self):
        self.get_lucky_archer().increase_count_luck

    def increase_count_luck(self):
        self.count_luck +=1

    def grant_throw_by_lucky_archer(self, round):
        archer = self.get_lucky_archer()
        self.score += archer.individual_launch()
        archer.increase_won_raffles(round)
        archer.increase_count_luck()

    def give_extra_throw_by_three_throws(self):
        for archer in self.archers:
            if archer.get_won_raffles() == 3:
                self.score += archer.individual_launch();


    def obtain_most_scored_archer(self):
        most_scored_archer = self.archers[0]
        for i in range (len(self.arches)):
            if self.arches[i].get_round_points() > most_scored_archer.get_round_points():
                most_scored_archer = archers[i]
        return most_scored_archer

    def obtain_most_won_rounds(self):
        most_won_rounds_archer = self.archers[0]
        for i in range (len(self.arches)):
            if self.arches[i].get_round_points() > most_won_rounds_archer.get_won_rounds():
                most_won_rounds_archer = self.arches[i]
        return most_won_rounds_archer

    def obtain_round_score(self):
        round_score = 0
        for archer in self.archers:
            round_score += archer.get_round_points()
        return round_score

    def obtain_total_score(self):
        total_score = 0
        for archer in self.arches:
            total_score += archer.get_points()
        return total_score

    def obtain_most_luck_archer(self):
        target = self.arches[0]
        for i in range (len(self.arches)):
            target = self.archers[i] if self.arches[i].get_count_luck > target.getCountLuck() else target
        return target

    def obtain_most_experienced(self):
        most_experienced_archer = self.archers[0]
        for i in range (len(self.arches)):
            if self.arches[i].get_experience() > most_experienced_archer.get_experience():
                most_experienced_archer = self.arches[i]
        return  most_experienced_archer


    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
    def get_code(self):
        return self.code

    def get_archers(self):
        return self.archers

    def get_won_rounds(self):
        return self.won_rounds

    def increase_won_rounds(self):
        self.won_rounds += 1

    def decrease_resistance_by_experience(self):
        for archer in self.arches:
            if archer.get_experience() == 0:
                archer.decrease_resistance_by_experience()

    def regain_round_points(self):
        for archer in self.arches:
            archer.regain_round_points()




# Crear instancias de Archer
archer1 = shot.Shot(0.8)
archer2 = shot.Shot(0.9)
archer3 = shot.Shot(0.7)

# Crear una lista de arqueros
archers = [archer1, archer2, archer3]

# Crear un equipo con la lista de arqueros
team = Team(archers, 1)

# Obtener el arquero con más suerte en el equipo
lucky_archer = team.get_lucky_archer()

if lucky_archer:
    print(f"El arquero más afortunado tiene una suerte de {lucky_archer.get_luck()}")
else:
    print("No se encontró ningún arquero afortunado en el equipo.")