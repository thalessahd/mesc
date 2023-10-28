from models.Status import Status
# Monsters
# Level 1 = 20 points
baseMonster = Status(5, 5, 5, 5)
# Level 2 = 30 points
regularMonster = Status(7.5, 7.5, 7.5, 7.5)
# Level 3 = 40 points
hardMonster = Status(10, 10, 10, 10)


dataStatus = { 'baseMonster' : baseMonster, 
                'regularMonster' : regularMonster, 
                'hardMonster' : hardMonster }