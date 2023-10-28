from scripts.utils import *

class Class():
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