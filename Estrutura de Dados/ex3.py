"""
3) Suponha o código abaixo que manipula um objeto que representa um carrinho
de compras.

Para o programa acima, realize as seguintes inserçõ es (utilize os conceitos de
OO vistos sempre que possí vel):
(a) Defina a classe ProdutoEstoque, cujo objetos sã o criados das linhas 4 a 7. Um
produto, representado por esta classe, possui um nome, um valor e a quantidade
deste produto em estoque.
(b) Crie a classe EstoqueProdutos, cujo objeto é criado na linha 3. Esta classe deve
permitir que produtos possam ser armazenados, como indica o mé todo
adicionaProduto, chamado das linhas 4 a 7.
(c) Crie a classe CarrinhoCompra, a qual permitirá a adiçã o de produtos à partir de
um estoque. Esta classe precisará implementar, pelo menos, 3 mé todos:
adicionaItem(), (linhas 10 a 12), que adiciona um item ao carrinho;
finalizaCompra(), (linha 13), que debita efetivamente a quantidade do produto
no estoque da quantidade comprada, e; calculaTotal(), (linha 15), que dá o
cô mputo total dos produtos (soma dos valores * a quantidade destes).

"""

class ProdutoEstoque():
    def __init__(self, nome, valor, qnt):
        self.nome = nome
        self.valor = valor
        self.quantidade = qnt

class EstoqueProdutos():
    def __init__(self):
        self.estoque = {} # Ex: {'monitor': ProdutoEstoque('monitor', 100, 200), 
                     #      'mouse': ProdutoEstoque('mouse', 70, 150)}

    def adicionaProduto(self, produto):
        self.estoque[produto.nome] = produto

class CarrinhoCompra():
    def __init__(self, estoque):
        self.Estoque = estoque
        self.carrinho = []
        self.erro = False
        self.erroMsg = []

    def adicionaItem(self, nomeProduto, qnt):
        self.carrinho.append([nomeProduto, qnt]) # Ex: [['monitor', 2], ['mouse', 3]]
    
    def finalizaCompra(self):
        self.erro = False
        for item in self.carrinho:
            produto = self.Estoque.estoque[item[0]]
            if (item[1] < produto.quantidade): # qtnProdCarrinho < qntProdEstoque ?
                produto.quantidade = produto.quantidade - item[1]
            else:
                self.erro = True
                self.erroMsg.append(f"Não foi possível adquirir {item[1]} unidades do produto {item[0]}.")

    def calculaTotal(self):
        if (self.erro):
            finalMsg = "Não foi possível calcular o total do carrinho :"
            for msg in self.erroMsg:
                finalMsg = finalMsg + '\n' + msg
            return finalMsg

        if (not self.carrinho):
            return "Carrinho vazio"
        else:
            total = 0.0
            for item in self.carrinho:
                produto = self.Estoque.estoque[item[0]]
                total = total + item[1] * produto.valor

            return total

def main():
    estoque = EstoqueProdutos()
    estoque.adicionaProduto(ProdutoEstoque("monitor", 500, 100))
    estoque.adicionaProduto(ProdutoEstoque("telefone", 150, 300))
    estoque.adicionaProduto(ProdutoEstoque("teclado", 70, 50))
    estoque.adicionaProduto(ProdutoEstoque("mouse", 50, 50))
    
    carrinho = CarrinhoCompra(estoque)
    carrinho.adicionaItem("monitor", 2)
    carrinho.adicionaItem("telefone", 5)
    carrinho.adicionaItem("teclado", 2)

    carrinho.finalizaCompra()
    print("A soma dos produtos : " + str(carrinho.calculaTotal()))

# Chamar main
main()