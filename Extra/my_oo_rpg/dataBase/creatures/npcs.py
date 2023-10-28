from models.NPC import NPC
from dataBase.status.status import dataStatus

greenSmile = NPC("Gosma Verde", 50, 20, dataStatus['baseMonster'])
goblin = NPC("Goblin", 80, 30, dataStatus['regularMonster'])
grayWolf = NPC("Lobo Cinza das Montanhas", 100, 50, dataStatus['hardMonster'])

dataNpcs = { 'greenSmile' : greenSmile,
             'goblin' : goblin,
             'grayWolf' : grayWolf }