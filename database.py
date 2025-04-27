import mysql.connector
import datetime

def conectar():
    conexao = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password ='',
        database = 'cadastro'
    )
    return conexao

def inserir_cliente(nome_cliente, email):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'INSERT INTO cadastro.cliente (nome, email, data_cadastro) VALUES ("{nome_cliente}", "{email}", "{datetime.datetime.now()}")'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def inserir_fornecedor(nome_fornecedor, email_fornecedor):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'INSERT INTO cadastro.fornecedores (nome, email, data_cadastro) VALUES ("{nome_fornecedor}", "{email_fornecedor}", "{datetime.datetime.now()}")'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def inserir_produto(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor_produto):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'INSERT INTO cadastro.produto (nome, data_cadastro, nome_usuario, descricao, quantidade, valor) VALUES ("{nome_produto}", "{datetime.datetime.now()}", "{nome_usuario}", "{descricao_produto}", {quantidade_produto}, {valor_produto})'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def listar_clientes():
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM cliente'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

def listar_fornecedores():
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM fornecedores'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados

def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'SELECT * FROM produto'
    cursor.execute(comando)
    resultados = cursor.fetchall()
    conexao.close()
    return resultados