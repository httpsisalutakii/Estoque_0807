from classe_compra import *
from classe_venda import *

class Menu:
    def __init__(self):
        estoque = Estoque()
        compra = Compra()
        venda = Venda ()

        compra.entrada_estoque = estoque
        venda.saida_estoque = estoque

        while True:
            entrada = input('1 - Cadastrar'
                            '\n2 - Buscar Produto'
                            '\n3 - Alterar Produto'
                            '\n4 - Entrada de Produto'
                            '\n5 - Saida de Produto'
                            '\n6 - sair\n')

            if entrada == '1':
                estoque.cadastrar_produtos()
            elif entrada == '2':
                estoque.listar_produtos()
            elif entrada == '3':
                pass
            elif entrada == '4':
                compra.comprar()
            elif entrada == '5':
                venda.vender()
            elif entrada == '0':
                break
            else:
                print('Opção invalida!!!')