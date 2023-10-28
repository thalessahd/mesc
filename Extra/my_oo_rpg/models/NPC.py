from models.Creature import Creature

class NPC(Creature):
    def __init__(self, name, hp, mp, status):
        super().__init__(name, hp, mp, status)
        self.speech = []

    def __str__(self):
        strNPC = f'Nome: {self.name}\nHP: {self.hp}\nMP: {self.mp}'
        return strNPC

    # Retorna uma fala do NPC
    def talk():
        pass