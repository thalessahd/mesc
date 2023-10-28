def getNameList(myList):
    aux = list(map( lambda x: x.name, myList))
    return ', '.join(aux)