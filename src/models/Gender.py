from enum import Enum


class Gender(Enum):
    FEMALE = 'F'
    MALE = 'M'

    def __init__(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender