from models.Creature import Creature

class NPC(Creature):
    """
    Representa uma criatura não jogável do jogo. Um monstro que precisa ser derrotado ou um aliado.

    Attributes
    ----------
    speech : str[]
        lista de falas do NPC
    """
    def __init__(self, name, hp, mp, status):
        super().__init__(name, hp, mp, status)
        self.speech = []

    def __str__(self):
        strNPC = f'Nome: {self.name}\nHP: {self.hp}\nMP: {self.mp}'
        return strNPC

    # Retorna uma fala do NPC
    def talk():
        pass