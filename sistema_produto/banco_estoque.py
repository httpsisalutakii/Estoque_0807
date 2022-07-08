from classe_fabricante import *
from classe_produto import *
import mysql.connector

class db_estoque:
    def __init__(self):
        # conexão
        self.db_estoque = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='estoque'
        )

        # conector
        self.cursor = self.db_estoque.cursor()

    def cadastrar_fabricante(self, nome, codigo, descricao, produto):
        obj_fabricante = Fabricante(nome, codigo, descricao, produto)
        comando_sql = f'insert into Fabricante ' \
                      f'(nome, descricao, produto) value ' \
                      f'({obj_fabricante.nome}", "{obj_fabricante.descricao}", "{obj_fabricante.produto}")'
        self.cursor.execute(comando_sql)
        self.db_estoque.commit()


    def cadastrar_produto(self, codigo, descricao, fabricante):
        obj_produto = Produto(codigo, descricao, fabricante)
        comando_sql = f'insert into Produtos ' \
                      f'(descricao, quantidade) value ' \
                      f'("{obj_produto.descricao}", "{obj_produto.fabricante}")'
        self.cursor.execute(comando_sql)
        self.db_estoque.commit()