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

def atualizar_cliente(nome_cliente, email, id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando1 = f'UPDATE cliente SET nome = "{nome_cliente}" WHERE id = "{id}"'
    comando2 = f'UPDATE cliente SET email = "{email}" WHERE id = "{id}"'  
    cursor.execute(comando1)
    cursor.execute(comando2)
    conexao.commit()
    conexao.close()

def atualizar_fornecedor(nome_fornecedor, email, id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando1 = f'UPDATE fornecedores SET nome = "{nome_fornecedor}" WHERE id = "{id}"'
    comando2 = f'UPDATE fornecedores SET email = "{email}" WHERE id = "{id}"'  
    cursor.execute(comando1)
    cursor.execute(comando2)
    conexao.commit()
    conexao.close()

def atualizar_produto(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor, id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando1 = f'UPDATE produto SET nome = "{nome_produto}" WHERE id = "{id}"'
    comando2 = f'UPDATE produto SET descricao = "{descricao_produto}" WHERE id = "{id}"'
    comando3 = f'UPDATE produto SET nome_usuario = "{nome_usuario}" WHERE id = "{id}"'
    comando4 = f'UPDATE produto SET quantidade = "{quantidade_produto}" WHERE id = "{id}"'  
    comando5 = f'UPDATE produto SET valor = "{valor}" WHERE id = "{id}"'  
    cursor.execute(comando1)
    cursor.execute(comando2)
    cursor.execute(comando3)
    cursor.execute(comando4)
    cursor.execute(comando5)
    conexao.commit()
    conexao.close()

def remove_cliente(id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'DELETE FROM cliente WHERE id ="{id}"'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def remove_fornecedor(id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'DELETE FROM fornecedores WHERE id ="{id}"'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()

def remove_produto(id):
    conexao = conectar()
    cursor = conexao.cursor()
    comando = f'DELETE FROM produto WHERE id ="{id}"'
    cursor.execute(comando)
    conexao.commit()
    conexao.close()