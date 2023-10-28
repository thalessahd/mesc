class Creature():
    def __init__(self, name, hp, mp, status):
        self.name = name
        self.level = 1
        self.hp = hp
        self.mp = mp
        self.status = status
        self.items = []

    # Ação de atacar, geralmente causa dano no alvo
    def attack():
        pass

    # Subir de nível, isso resulta em aumento dos status, aprender novos skills e adquirir novos itens
    def levelUp():
        pass
    
    # Usar um item que existe na mochila
    def useItem():
        pass