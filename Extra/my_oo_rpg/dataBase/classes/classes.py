from models.Class import Class
from dataBase.status.playerStatus import dataStatus as dataPlayerStatus
from dataBase.skills.warrior import dataSkills as warriorSkills
from dataBase.skills.mage import dataSkills as mageSkills
from dataBase.skills.archer import dataSkills as archerSkills

warrior = Class('Guerreiro', dataPlayerStatus['baseStatusWarrior'])
warrior.setSkill(warriorSkills[1])

mage = Class('Mago', dataPlayerStatus['baseStatusMage'])
mage.setSkill(mageSkills[1])

archer = Class('Arqueiro', dataPlayerStatus['baseStatusArcher'])
archer.setSkill(archerSkills[1])

dataClasses = { 'warrior' : warrior, 
                'mage' : mage, 
                'archer' : archer}