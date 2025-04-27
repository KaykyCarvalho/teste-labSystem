import os
import database
import terminal
import time
import visualizacao_clientes
import visualizacao_fornecedores
import visualizacao_produtos

def obter_numero_inteiro():
    while True:
        try:
            qtd = int(input("| Digite a quantidade desse produto: "))
            if(qtd < 0):
                raise ValueError
            return qtd
        except ValueError:
            print("DIGITE UM NÚMERO INTEIRO!")

def obter_numero_real():
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


def cadastrar_produto():
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
    database.inserir_produto(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor_produto)
    limpar_terminal()
    print(nome_produto, 'adicionado(a) com sucesso.')
    time.sleep(5)

def visualizar_clientes():
    limpar_terminal()
    resultados = database.listar_clientes()
    tabela = visualizacao_clientes.tabela_formata(resultados)
    print(tabela)
    print('')
    input("Pressione Enter para voltar ao menu principal.")

def visualizar_fornecedores():
    limpar_terminal()
    resultados = database.listar_fornecedores()
    tabela = visualizacao_fornecedores.tabela_formata(resultados)
    print(tabela)
    print('')
    input("Pressione Enter para voltar ao menu principal.")

def visualizar_produtos():
    limpar_terminal()
    resultados = database.listar_produtos()
    tabela = visualizacao_produtos.tabela_formata(resultados)
    print(tabela)
    print('')
    input("Pressione Enter para voltar ao menu principal.")

def modificar_cliente():
    limpar_terminal()
    resultados = database.listar_clientes()
    tabela = visualizacao_clientes.tabela_formata(resultados)
    print(tabela)
    print('')
    id = int(input("Digite o ID do cliente que deseja modificar: "))
    print('')
    nome_cliente = input("Digite o novo nome do cliente: ")
    print('')
    email = input("Digite o novo Email do cliente: ")
    print('')
    database.atualizar_cliente(nome_cliente, email, id)
    print(nome_cliente, 'modificado(a) com sucesso.')
    print('')
    input("Pressione Enter para voltar ao menu principal. ")

def modificar_fornecedor():
    limpar_terminal()
    resultados = database.listar_fornecedores()
    tabela = visualizacao_fornecedores.tabela_formata(resultados)
    print(tabela)
    print('')
    id = int(input("Digite o ID do fornecedor que deseja modificar: "))
    print('')
    nome_fornecedor = input("Digite o novo nome do fornecedor: ")
    print('')
    email = input("Digite o novo Email do fornecedor: ")
    print('')
    database.atualizar_fornecedor(nome_fornecedor, email, id)
    print(nome_fornecedor, 'modificado(a) com sucesso.')
    print('')
    input("Pressione Enter para voltar ao menu principal. ")

def modificar_produto():
    limpar_terminal()
    resultados = database.listar_produtos()
    tabela = visualizacao_produtos.tabela_formata(resultados)
    print(tabela)
    print('')
    id = int(input("Digite o ID do produto que deseja modificar: "))
    print('')
    nome_produto = input("Digite o nome do produto : ")
    print('')
    descricao_produto = input("Descrição do produto : ")
    print('')
    quantidade_produto = obter_numero_inteiro()
    print('')
    valor_produto = obter_numero_real() 
    print('')
    nome_usuario = input("Responsavel pela adição do produto: ")
    print('')
    database.atualizar_produto(nome_produto, nome_usuario, descricao_produto, quantidade_produto, valor_produto, id)
    print(nome_produto, 'modificado(a) com sucesso.')
    print('')
    input("Pressione Enter para voltar ao menu principal. ")

def remover_cliente():
    limpar_terminal()
    resultados = database.listar_clientes()
    tabela = visualizacao_clientes.tabela_formata(resultados)
    print(tabela)
    print('')
    id = int(input("Digite o ID do cliente que deseja remover: "))
    database.remove_cliente(id)
    print('')
    print('Cliente removido com sucesso.')
    print('')
    input("Pressione Enter para voltar ao menu principal. ")

def remover_fornecedor():
    limpar_terminal()
    resultados = database.listar_fornecedores()
    tabela = visualizacao_fornecedores.tabela_formata(resultados)
    print(tabela)
    print('')
    id = int(input("Digite o ID do fornecedor que deseja remover: "))
    database.remove_fornecedor(id)
    print('')
    print('Fornecedor removido com sucesso.')
    print('')
    input("Pressione Enter para voltar ao menu principal. ")

def remover_produto():
    limpar_terminal()
    resultados = database.listar_produtos()
    tabela = visualizacao_produtos.tabela_formata(resultados)
    print(tabela)
    print('')
    id = int(input("Digite o ID do produto que deseja remover: "))
    database.remove_produto(id)
    print('')
    print('Produto removido com sucesso.')
    print('')
    input("Pressione Enter para voltar ao menu principal. ")