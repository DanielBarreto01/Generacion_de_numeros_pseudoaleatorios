from typing import List
from Archer import Archer

class Team:
        
    def __init__(self, archers: List[Archer], code: int):
        self.archers = archers
        self.code = code
        self.score = 0
        self.won_rounds = 0
    
    """Incrementa el número de rondas ganadas por el equipo."""
    def increase_won_rounds(self):
        
        self.won_rounds += 1

    """Obtiene al arquero con más suerte en el equipo."""
    def get_lucky_archer(self) -> Archer:
        lucky_archer = None
        max_luck = 0
        for archer in self.archers:
            if archer.get_luck() > max_luck:
                max_luck = archer.get_luck()
                lucky_archer = archer
        return lucky_archer
    
    """Incrementa la suerte del arquero más afortunado."""
    def increase_luck_to_archer(self):
        lucky_archer = self.get_lucky_archer()
        if lucky_archer:
            lucky_archer.increase_count_luck()

    """ Otorga un lanzamiento adicional al arquero más afortunado."""
    def grant_throw_by_lucky_archer(self, round: int):
        lucky_archer = self.get_lucky_archer()
        if lucky_archer:
            self.score += lucky_archer.individual_launch()
            lucky_archer.increase_won_raffles(round)
            lucky_archer.increase_count_luck()

    """Otorga un lanzamiento extra a los arqueros que han ganado 3 tiros. """
    def give_extra_throw_by_three_throws(self):

        for archer in self.archers:
            if archer.get_won_raffles() == 3:
                self.score += archer.individual_launch()

    """Obtiene al arquero con la puntuación más alta en una ronda.
        """
    def obtain_most_scored_archer(self) -> Archer:
        most_scored_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.get_round_points() > most_scored_archer.get_round_points():
                most_scored_archer = archer
        return most_scored_archer
    
    """Obtiene al arquero con más rondas ganadas en el equipo."""
    def obtain_most_won_rounds_archer(self) -> Archer:
        most_won_rounds_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.get_won_rounds() > most_won_rounds_archer.get_won_rounds():
                most_won_rounds_archer = archer
        return most_won_rounds_archer

    """Obtiene la puntuación total del equipo en una ronda."""
    def obtain_round_score(self) -> int:
        round_score = 0
        for archer in self.archers:
            round_score += archer.get_round_points()
        return round_score
    
    """Obtiene la puntuación total del equipo en todas las rondas. """
    def obtain_total_score(self) -> int:
        total_score = 0
        for archer in self.archers:
            total_score += archer.get_points()
        return total_score

    """ Obtiene al arquero más afortunado en el equipo."""
    def obtain_most_luck_archer(self) -> Archer:

        most_luck_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.get_count_luck() > most_luck_archer.get_count_luck():
                most_luck_archer = archer
        return most_luck_archer
    
    """Obtiene al arquero más experimentado en el equipo. """
    def obtain_most_experienced_archer(self) -> Archer:
        most_experienced_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.get_experience() > most_experienced_archer.get_experience():
                most_experienced_archer = archer
        return most_experienced_archer
