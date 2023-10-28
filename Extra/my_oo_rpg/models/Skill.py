class Skill():
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