import terminal # mostra as telas no terminal
import database # Banco de dados
import metodos # Busca métodos separados
import os # Envia comandos direto no terminal
import time # Cria timer

while True:
    terminal.menu_inicial()
    r = int(input("Escolha uma das opções acima: "))
    if r == 1:
        metodos.cadastrar_cliente()
    elif r == 2:
        metodos.cadastrar_fornecedor()
    elif r == 3:
        metodos.criar_produto()
    elif r == 4:
        metodos.visualizar_produtos()
    elif r == 5:
        terminal.sobre_o_candidato()
    else:
        metodos.limpar_terminal()
        print("tente novamente...")
        time.sleep(10)