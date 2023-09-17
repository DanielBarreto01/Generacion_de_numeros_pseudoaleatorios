from enum import Enum


class Shoot(Enum):
    CENTRAL = 10
    INTERMEDIATE = 9
    OUTSIDE = 8
    ERROR = 0
    def __init__(self, score):
        self.score = score;



    def get_score(self):
        return self.score;