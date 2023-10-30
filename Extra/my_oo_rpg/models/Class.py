from scripts.utils import *

class Class():
    """
    Representa uma classe que o Player pode ser. A classe define os Status base e os skills do
    personagem.

    Attributes
    ----------
    name : str
        nome da classe
    Skills : Skill[]
        lista das skills da classe
    baseStatus : Status
        status base da classe
    """
    def __init__(self, name, baseStatus):
        self.name = name
        self.skills = []
        self.baseStatus = baseStatus

    def __str__(self):
        skills = getNameList(self.skills)
        strClass = f'Classe: {self.name}\n--Status:--{self.baseStatus}\nSkills: [{skills}]'
        return strClass

    # Definir um skill para a classe
    def setSkill(self, Skill):
        self.skills.append(Skill)