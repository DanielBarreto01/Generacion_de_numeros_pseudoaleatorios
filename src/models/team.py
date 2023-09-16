import shot
class Team:
    def __init__(self, arches, code):
        # self.arches[0] = shot.Shot(5).
        self.arches = arches
        self.code = code
        self.score=0
        self.won_rounds = 0

    def get_lucky_archer(self):
        lucky_archer = None
        max_lucky = 0
        for i in self.arches:
            if i.generate_gender() > max_lucky:
                max_lucky = 5
                lucky_archer = i
        return lucky_archer


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