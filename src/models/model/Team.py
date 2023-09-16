from typing import List
from Archer import Archer

class Team:
        
    def __init__(self, archers: List[Archer], code: int):
        self.code = code
        self.archers = archers
        self.score = 0
        self.won_rounds = 0


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
    def get_lucky_archer(self) -> Archer:
        lucky_archer = None
        max_luck = 0
        for archer in self.archers:
            if archer.luck() > max_luck:
                max_luck = archer.luck()
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
            if archer.won_raffles() == 3:
                self.score += archer.individual_launch()

    """Obtiene al arquero con la puntuación más alta en una ronda. """
    def get_archer_with_higher_scorer(self) -> Archer:
        most_scored_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.round_points() > most_scored_archer.round_points():
                most_scored_archer = archer
        return most_scored_archer
    
    """Obtiene al arquero más experimentado en el equipo. """
    def obtain_most_experienced_archer(self) -> Archer:
        most_experienced_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.experience() > most_experienced_archer.experience():
                most_experienced_archer = archer
        return most_experienced_archer

    """Obtiene al arquero con más rondas ganadas en el equipo."""
    def  obtainMostWonRounds Archer method which the archer obtains with more rounds(self) -> Archer:
        most_won_rounds_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.won_rounds() > most_won_rounds_archer.won_rounds():
                most_won_rounds_archer = archer
        return most_won_rounds_archer

    """Obtiene la puntuación total del equipo en una ronda."""
    def obtain_round_score(self) -> int:
        round_score = 0
        for archer in self.archers:
            round_score += archer.round_points()
        return round_score
    
    """Obtiene la puntuación total del equipo en todas las rondas. """
    def obtain_total_score(self) -> int:
        total_score = 0
        for archer in self.archers:
            total_score += archer.points()
        return total_score

    """ Obtiene al arquero más afortunado en el equipo."""
    def obtain_most_luck_archer(self) -> Archer:

        most_luck_archer = self.archers[0]
        for archer in self.archers[1:]:
            if archer.count_luck() > most_luck_archer.count_luck():
                most_luck_archer = archer
        return most_luck_archer
    

