class Status():
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