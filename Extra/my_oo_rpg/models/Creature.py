class Creature():
    """
    Representa uma criatura do jogo, podendo ser um Player(jogável) ou um NPC(não jogável)

    Attributes
    ----------
    name : str
        nome da criatura
    level : int
        indica o level da criatura
    hp : int
        pontos de saúde da criatura, se for 0 a criatura está morta
    mp : int
        pontos de mágia da criatura. Esses pontos são gastos pelas skills.
    status : Status
        status da criatura
    items : Item[]
        lista de itens que a criatura tem em sua posse
    """
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