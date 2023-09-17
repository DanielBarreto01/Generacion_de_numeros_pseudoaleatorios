from src.models import archer


class Team:

    def __init__(self, archers, code: int):
        self.archers = archers
        self.code = code
        self.score=0
        self.won_rounds = 0
        self.count_luck = 0


    """ le da  lanzamiento adicional al arquero más afortunado."""
    def launch_by_luck(self, round: int):
        lucky_archer = self.get_lucky_archer()
        if lucky_archer:
            self.score += lucky_archer.individual_launch()
            lucky_archer.increase_won_raffles(round)
            lucky_archer.increase_count_luck()

    """Incrementa el número de rondas ganadas por el equipo."""
    def increase_won_rounds(self):
        self.won_rounds += 1

    """Obtiene al arquero con más suerte en el equipo."""
    def get_lucky_archer(self) -> archer:
        lucky_archer = None
        max_luck = 0
        for archer in self.archers:
            if archer.luck > max_luck:
                max_luck = archer.luck
                lucky_archer = archer
        return lucky_archer

    """Incrementa la suerte del arquero más afortunado."""   #RARRO
    def increase_luck_to_archer(self):
        lucky_archer = self.get_lucky_archer()
        if lucky_archer:
            lucky_archer.increase_count_luck()



    """Otorga un lanzamiento extra a los arqueros que han ganado 3 tiros. """
    def give_extra_throw_by_three_throws(self):

        for archer in self.archers:
            if archer.won_raffles == 3:
                self.score += archer.individual_launch()

    """Obtiene al arquero con la puntuación más alta en una ronda. """
    def get_archer_with_higher_scorer(self) -> archer:
        most_scored_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.round_points > most_scored_archer.round_points:
                most_scored_archer = archer
        return most_scored_archer

    "restaura puntos ronda"
    def regain_round_points(self):
        for archer in self.archers:
            archer.regain_round_points()

    """Obtiene al arquero más experimentado en el equipo. """
    def obtain_most_experienced_archer(self) -> archer:
        most_experienced_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.experience() > most_experienced_archer.experience():
                most_experienced_archer = archer
        return most_experienced_archer

    """reduce resistencia de arqueros por experiencia."""       #validarr
    def decrease_resistance_experience(self):
        for archer in self.archers:
            if archer.experience == 0:
                archer.decrease_resistance_by_experience()

    """Obtiene al arquero con más rondas ganadas en el equipo."""
    def obtain_most_won_rounds_archer(self) -> archer:
        most_won_rounds_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.won_rounds > most_won_rounds_archer.won_rounds:
                most_won_rounds_archer = archer
        return most_won_rounds_archer

    """Obtiene la puntuación total del equipo en una ronda."""
    def obtain_round_score(self) -> int:
        round_score = 0
        for archer in self.archers:
            round_score += archer.round_points
        return round_score

    """Obtiene la puntuación total del equipo en todas las rondas. """
    def obtain_total_score(self) -> int:
        total_score = 0
        for archer in self.archers:
            total_score += archer.points()
        return total_score

    """ Obtiene al arquero más afortunado en el equipo."""
    def obtain_most_luck_archer(self) -> archer:
        most_luck_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.count_luck() > most_luck_archer.count_luck():
                most_luck_archer = archer
        return most_luck_archer




# Crear instancias de Archer
archer1 = archer.Archer(0.8)
archer2 = archer.Archer(0.9)
archer3 = archer.Archer(0.7)

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