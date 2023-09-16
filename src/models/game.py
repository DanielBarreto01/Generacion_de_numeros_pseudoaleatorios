from typing import List
from Team import Team
from Archer import Archer
from Gender import Gender
from Score import Score

class Game:
    def __init__(self, team1: Team, team2: Team):
        self.teams = [team1, team2]
        self.rounds = 1
        self.winnerGender = None

    """Realiza el sorteo de lanzamientos entre los equipos."""
    def raffle_shoot(self):
        for team in self.teams:
            team.launch_by_luck(self.rounds)

    """Determina el arquero ganador de la ronda."""
    def determine_round_winner_archer(self):
        winner = None
        archer_team_1 = self.teams[0].get_archer_with_higher_scorer()
        archer_team_2 = self.teams[1].get_archer_with_higher_scorer()

        if archer_team_1.round_points == archer_team_2.round_points:
            winner = self.check_tie(archer_team_1, archer_team_2)
        else:
            winner = archer_team_1 if archer_team_1.round_points > archer_team_2.round_points else archer_team_2
        winner.gain_experience()


    """Realiza un desempate de arqueros ."""
    def check_tie(self, a: Archer, b: Archer) -> Archer:
        winner = None
        shootA = a.round_points()
        shootB = b.round_points()
        while shootA == shootB:
            shootA = a.individual_launch()
            shootB = b.individual_launch()
        winner = a if shootA > shootB else b
        winner.increase_won_rounds()
        return winner

    """Obtiene al arquero individual ganador del juego."""
    def obtain_individual_winner(self) -> Archer:
        archer_one = self.teams[0].obtain_most_won_rounds_archer()
        archer_thow = self.teams[1].obtain_most_won_rounds_archer()
        return archer_one if archer_one.won_rounds() > archer_thow.won_rounds() else archer_thow

    def obtain_experience_winner(self) -> Archer:
        """Obtiene al arquero más experimentado de los equipos."""
        archer_one = self.teams[0].obtain_most_experienced_archer()
        archer_thow = self.teams[1].obtain_most_experienced_archer()
        return archer_one if archer_one.experience() >  archer_thow.experience() else  archer_thow

    def determine_team_round_winner(self):
        """Determina al equipo ganador de la ronda."""
        score_team_one = self.teams[0].obtain_round_score()
        score_team_thow = self.teams[1].obtain_round_score()
        self.teams[0].score += score_team_one
        self.teams[1].score += score_team_thow
        teamWinner = self.teams[0] if score_team_one > score_team_thow else self.teams[1]
        if teamWinner is not None:
            teamWinner.increase_won_rounds()

    """Obtiene al equipo ganador del juego."""
    def obtain_team_winner(self) -> Team:
        scoreTeam1 = self.teams[0].obtain_total_score()
        scoreTeam2 = self.teams[1].obtain_total_score()
        return self.teams[0] if scoreTeam1 > scoreTeam2 else self.teams[1] if scoreTeam1 < scoreTeam2 else None

    def determine_win_Gender(self):
        self.winnerGender = self.obtain_individual_winner().gender()

    """Obtiene al arquero más afortunado de los 2 equipos."""
    def obtain_most_luck_archer(self) -> Archer:
        countLuckArcherTeam1 = self.teams[0].obtain_most_luck_archer()
        countLuckArcherTeam2 = self.teams[1].obtain_most_luck_archer()
        return (
            countLuckArcherTeam1
            if countLuckArcherTeam1.count_luck() == countLuckArcherTeam2.count_luck()
            else countLuckArcherTeam1
            if countLuckArcherTeam1.count_luck() > countLuckArcherTeam2.count_luck()
            else countLuckArcherTeam2
        )

    """Obtiene la puntuación del equipo en una posición específica."""
    def obtain_team_score(self, position: int) -> int:
        return self.teams[position].score()

    """Obtiene un equipo en una posición específica."""
    def obtain_team(self, position: int) -> Team:
        return self.teams[position]

    """Incrementa el número de rondas en 1 unidad."""
    def increase_rounds(self):
        self.rounds += 1

    """Otorga un tiro extra a cada equipo."""
    def give_extra_throwBy_three_throws(self):
        self.teams[0].give_extra_throw_by_three_throws()
        self.teams[1].give_extra_throw_by_three_throws()

    def decrease_resistance_Experience(self):
        """Reduce la resistencia por experiencia de cada equipo."""
        self.teams[0].decrease_resistance_experience()
        self.teams[1].decrease_resistance_experience()


    """Restaura los puntos de la ronda para cada equipo."""
    def regain_round_points(self):
        for team in self.teams:
            team.regain_round_points()

    def get_winner_gender(self) -> Gender:
        """Obtiene el género del ganador del juego."""
        return self.winnerGender

    def get_archers(self) -> List[Archer]:
        """Obtiene a todos los arqueros de ambos equipos."""
        archers = []
        for team in self.teams:
            for archer in team.archers():
                archers.append(archer)
        return archers