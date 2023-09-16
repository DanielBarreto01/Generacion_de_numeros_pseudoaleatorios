from typing import List, Any

from src.models import archer, game, Gender
class Simulation:
    def __init__(self, games):
        self.list_game = []
        self.count_won_rounds_male = 0
        self.count_won_rounds_female = 0
        self.total_points_team1 = 0
        self.total_points_team2 = 0
        self.init_simulation(games)
        self.team1 = None
        self.team2 = None


    #Método initTeams void que inicializa cada equipo desde cero.
    def init_teams(self):
        self.team1 = [archer.Archer(1), archer.Archer(2), archer.Archer(3), archer.Archer(4), archer.Archer(5), 1]
        self.team2 = [archer.Archer(6), archer.Archer(7), archer.Archer(8), archer.Archer(9), archer.Archer(10), 2]

    """
        initSimulation void method that contains all the simulation logic.

    @param games."""

    def init_simulation(self,games):
        for i in range(games):
            self.init_teams()
            current_game = game.Game(self.team1, self.team2)
            self.list_game.append(current_game) # // Add new game to list
            for j in range(10): #// Rounds loop
                for team in self.list_game[j].teams:
                    for archer in team.get_archers():
                        archer.launch()
                current_game.raffle_shoot()
                if j >= 2:
                    current_game.give_extra_throwBy_three_throws() #Give extra shoot
                current_game.determine_round_winner_archer()
                current_game.determine_team_round_winner()
                current_game.increase_rounds()
                current_game.regain_round_points()
            current_game.determine_win_Gender()


        """obtainTotalWinByGender Gender method that gets the winning gender per game
        and counts it.
        @return Gender."""


    def obtain_total_win_by_gender(self):
        for game in self.list_game:
            if game.get_winner_gender().get_gender() == 'M':
                self.count_won_rounds_male += 1
            else:
                self.count_won_rounds_female += 1
        return Gender.Gender().MAlE if self.count_won_rounds_male > self.count_won_rounds_female else Gender.Gender().FEMALE

        """/**
        *
        * determineTeamWinner void method that counts the total points of all games.
        */
        """
    def determine_team_winner(self):
        for game in self.list_game:
            self.total_points_team1 += game.obtain_team_score(0)
            self.total_points_team2 += game.obtain_team_score(1)

    """/**
    *
    * obtainLuckyArchers String method that gets the list of lucky archers in each
    * game in a String.
    *
    * @return String.
    */"""

    def obtain_lucky_archers(self):
        lucky_archers_string = ""
        for i in range (len(self.list_game)):
            lucky_archers_string += f"Game {i+1} :Archer {self.list_game[i].oobtain_most_luck_archer().code} \n"
        return lucky_archers_string

    """/**
    *
    * obtainExperiencedArchers String methodgets the most experienced archers in a
    * String.
    *
    * @return String.
    */"""

    def obtain_experienced_archers(self):
        experience_archers_string = ""
        for i in range(len(self.list_game)):
            experience_archers_string += f"Game {i+1} : arquero {self.list_game[i].obtain_experience_winner().code} \n"
        return experience_archers_string

    """/**
    *
    * obtainWinnerTeam String method that gets the winning team of all games in a
    * String.
    *
    * @return String.
    */"""

    def obtainWinningTeam(self):
        self.determine_team_winner()
        target_team = None
        target_points = 0
        if self.total_points_team1 > self.total_points_team2:
            target_team = self.team1
            target_points = self.total_points_team1
        else:
            target_team = self.team2
            target_points = self.total_points_team2

        return  f"TEAM  {target_team.get_code}  with  {target_points:,} points";

    """/**
    *
    * obtainGenderTotalWin String method that returns message of the gender that
    * wins more games.
    *
    * @return String.
    */"""

    def obtain_gender_total_win(self):
        return "FEMALE" if self.obtain_total_win_by_gender().get_gender == 'F' else "MALE"

   """ /**
    *
    * obtainGendersByGame String method which gets a message setting the winning
    * gender per game.
    *
    * @return String.
    */"""

    def obtain_genders_by_game(self):
        genders_by_game_string = ""
        for i in range(len(self.list_game)):
            genders_by_game_string = f"Game {i+1} : {self.list_game[i].get_winner_gender().get_gender()} \n"
        return  genders_by_game_string



    """/**
    *
    * obtainArchersByGame Archer ArrayList method that gets the list of archers on
    * a specific game.
    * @param game.
    * @return Archer ArrayList.
    */"""

    def obtain_archers_by_game(self, game):
        return self.list_game[game-1].get_archers()

    """/**
    *
    * getArchersPerGame Archer ArrayList method that gets the list of archers per
    * game.
    * @return Archer ArrayList.
    */"""

    def get_archers_per_game(self):
        arches = []
        for game in self.list_game:
            for archer in game.get_archers():
                arches.append(archer)
        return arches


