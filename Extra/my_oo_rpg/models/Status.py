class Status():
    """
    Representa o status de uma criatura. Durante uma luta o status é usado para definir os pontos de HP
    e MP, a força e outros aspectos importantes durante o combate.

    Attributes
    ----------
    con : double
        Quanto mais pontos aqui, maior o HP da criatura
    str : double
        Quanto mais pontos aqui, maior a força da criatura
    int : double
        Quanto mais pontos aqui, maior o MP da criatura
    dex : double
        Quanto mais pontos aqui, maior as chances de desviar de um ataque
    """
    def __init__(self, con, str, int, dex):
        self.con = con
        self.str = str
        self.int = int
        self.dex = dex

    def __str__(self):
        strStatus = f'CON: {self.con}\nSTR: {self.str}\nINT: {self.int}\nDEX: {self.dex}\n'
        return strStatus

    # Aumentar os valores dos atributos da classe
    def upStatus():
        pass