class Item():
    """
    Representa um item do jogo.

    Attributes
    ----------
    name : str
        nome da criatura
    type : Enum
        tipo do item podendo ser uma das constantes [TYPE_DAMAGE, TYPE_HEALING]
    value : int
        valor de ação daquele item, seu efeito varia dependendo do tipo
    description : str
        descrição do item
    """
    TYPE_DAMAGE = 'Damage'
    TYPE_HEALING = 'Healing'

    def __init__(self, name, type, value, description):
        self.name = name
        self.type = type
        self.value = value
        self.description = description

    # Usar um item. O uso do item é diferente dependendo do seu type
    def use():
        pass

    # Retornar a descrição ou os atributos da classe
    def examine():
        pass

    # Escolher um item para jogar fora uma vez que a mochila tem uma capacidade máxima
    def drop():
        pass