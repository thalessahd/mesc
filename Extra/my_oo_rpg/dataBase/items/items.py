from models.Item import Item

potion = Item('Poção simples', Item.TYPE_HEALING, 10, 'Recupera poucos pontos de vida')
superPotion = Item('Poção média', Item.TYPE_HEALING, 20, 'Recupera uma quantidade razoável de vida')
hyperPotion = Item('Poção avançada', Item.TYPE_HEALING, 50, 'Recupera muitos pontos de vida')

rock = Item('Pedra pequena', Item.TYPE_DAMAGE, 10, 'Inflinge uma pequena quantia de dano')

dataItems = { 'potion' : potion, 
              'superPotion' : superPotion, 
              'hyperPotion' : hyperPotion,
              'rock' : rock}