from models.Creature import Creature

class Player(Creature):
    """
    Representa uma criatura jogável do jogo. Esse personagem será controlado por quem estiver jogando.

    Attributes
    ----------
    class : Class
        classe do personagem
    """
    def __init__(self, name, hp, mp, status, playerClass):
        super().__init__(name, hp, mp, status)
        self.playerClass = playerClass

    # Exibir quais itens estão na mochila do Player
    def checkItems():
        pass

    # Definir os status base do Player. Este varia de acordo com a classe do Player
    def setBasicStatus():
        pass