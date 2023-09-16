class Team:
    def __init__(self, arches, code):
        self.arches = arches
        self.code = code
        self.score=0
        self.won_rounds = 0

    def get_lucky_archer(self):
        maxLucky = 0
        for i in self.arches:
            if i.