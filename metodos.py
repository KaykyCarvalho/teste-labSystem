import os
import database
import terminal
import time
import formatacao

def obter_numero_inteiro(): # Função que verifica se o usuário digitou um número e inteiro
    while True:
        try:
            qtd = int(input("| Digite a quantidade desse produto: "))
            if(qtd < 0):
                raise ValueError
            return qtd
        except ValueError:
            print("DIGITE UM NÚMERO INTEIRO!")

def obter_numero_real(): # Função que verifica se o usuário digitou um número e inteiro
    while True:
        try:
            qtd = float(input("| Digite o valor desse produto: "))
            if(qtd < 0):
                raise ValueError
            return qtd
        except ValueError:
            print("DIGITE UM NÚMERO Inteiro OU Real !")

def limpar_terminal():
    os.system('cls||clear')

def cadastrar_cliente():
    limpar_terminal()
    terminal.adicionando_cliente()
    nome_cliente = input("| Digite o nome do cliente : ") 
    limpar_terminal()
    terminal.adicionando_cliente()
    email = input("| Email do cliente : ")
    limpar_terminal()
    database.inserir_cliente(nome_cliente, email)
    limpar_terminal()
    print(nome_cliente, 'adicionado(a) com sucesso.')
    time.sleep(5)

def cadastrar_fornecedor():
    limpar_terminal()
    terminal.adicionando_fornecedor()
    nome_fornecedor = input("| Digite o nome do fornecedor : ") 
    limpar_terminal()
    terminal.adicionando_fornecedor()
    email_fornecedor = input("| Email do fornecedor : ")
    limpar_terminal()
    database.inserir_fornecedor(nome_fornecedor, email_fornecedor)
    limpar_terminal()
    print(nome_fornecedor, 'adicionado(a) com sucesso.')
    time.sleep(5)


def criar_produto(): # CREATE | Criação de um novo produto, onde é solicitado nome do usuario, nome do produto, descricao do produto, quantidade do produto e valor do produto.
    limpar_terminal()
    terminal.adicionando_produto()
    nome_produto = input("| Digite o nome do produto : ") 
    limpar_terminal()
    terminal.adicionando_produto()
    print("| Ex: Marca, Modelo, Material, Utilidade, Config, etc.. ")
    descricao_produto = input("| Descrição do produto : ")
    limpar_terminal()
    terminal.adicionando_produto()
    quantidade_produto = obter_numero_inteiro()
    limpar_terminal()
    terminal.adicionando_produto()
    valor_produto = obter_numero_real() 
    limpar_terminal()
    terminal.adicionando_produto()
    nome_usuario = input("Responsavel pela adição do produto: ")
    database.inserir(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor_produto)
    limpar_terminal()
    print(nome_produto, 'adicionado(a) com sucesso.')
    time.sleep(5)

def visualizar_produtos():
    limpar_terminal()
    resultados = database.listar()
    tabela = formatacao.tabela_formata(resultados)
    print(tabela)
    time.sleep(10)