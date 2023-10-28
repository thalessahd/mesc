class Item():
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