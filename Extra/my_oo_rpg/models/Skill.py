class Skill():
    """
    Representa um skill do jogo. Uma habilidade que pode ser utilizada pelos Players caso cumpram
    com os requisitos.

    Attributes
    ----------
    name : str
        nome da skill
    type : Enum
        tipo da skill podendo ser uma das constantes [TYPE_DAMAGE, TYPE_HEALING, TYPE_BUFF, TYPE_DEBUFF]
    value : int
        valor de ação da skill, seu efeito varia dependendo do tipo
    description : str
        descrição da skill
    """
    TYPE_DAMAGE = 'Damage'
    TYPE_HEALING = 'Healing'
    TYPE_BUFF = 'Buff'
    TYPE_DEBUFF = 'Debuff'

    def __init__(self, name, type, value, description):
        self.name = name
        self.type = type
        self.value = value
        self.description = description
    
    def __str__(self):
        return self.name

    # Usar um skill. O efeito da skill é diferente dependendo do seu type
    def use():
        pass

    # Retornar a descrição ou os atributos da classe
    def examine():
        pass