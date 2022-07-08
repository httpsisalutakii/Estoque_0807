from classe_estoque import *

class Compra:
    def __init__(self):
        self.entrada_estoque = Estoque()

    def comprar(self):
        entrada = int(input('Informe o codigo do produto'))
        for i in range(len(self.entrada_estoque.listaProdutos)):
            if entrada == self.entrada_estoque.listaProdutos[i].cod:
                self.entrada_estoque.listaProdutos[i].quantidade += \
                int(input('Informea quantidade comprada'))
