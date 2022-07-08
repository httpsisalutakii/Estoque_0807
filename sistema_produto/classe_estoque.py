from classe_produto import *

class Estoque:
    def __init__(self):
        self.listaProdutos = []
        self.listaProdutos.append(Produto(1, 'Arroz'))
        self.listaProdutos.append(Produto(2, 'Feijão'))

    def cadastar(self):
        argumento1 = len(self.listaProdutos)+1
        argumento2 = input('Informe o codigo:')
        entrada_descricao = input('Informe a descrição')
        entrada_fabricante = input('Informe o fabricante')
        entrada_quantidade = input('Informe a quantidade')
        self.listaProdutos.append(Produto(argumento1, argumento2))
        print('Estoque salvo com sucesso!')

    def listar_produtos(self):
        for i in range(len(self.listaProdutos)):
            print('código', self.listaProdutos[i].codigo,
                  'descrição', self.listaProdutos[i].descricao,
                   'quantidade', self.listaProdutos[i].quantidade)
