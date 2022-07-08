class classe_estoque import *


class Venda:
    def __init__(self):
        self.saida_estoque = Estoque()

    def vender(self):
        entrada = int(input('Informe o codigo do produto:'))
        for i in range(len(self.saida_estoque.listaProdutos)):
            if entrada == self.saida_estoque.listaProdutos[i].codigo:
                self.saida_estoque.listaProdutos[i].quantidade -= int(input('Quantidade vendida: '))