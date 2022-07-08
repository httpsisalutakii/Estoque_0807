create database db_estoque;
use db_estoque

create table produto(
id_produto int,
descricao varchar (70),
fabricante varchar (30),
quantidade float);

create table fabricnte(
nome varchar (70),
id_fabricante int, 
descricao varchar(70),
produto varchar(30));

create table menu(
cadastar varchar(70),
listar_todos varchar (200),
procurar_produto varchar (200),
alterar_produto varchar(200),
sair bit );

create table historico_venda(
id_produto int);

create table historico_compra(
id_produto int);