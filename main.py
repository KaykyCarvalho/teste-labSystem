import terminal # mostra as telas no terminal
import metodos # Busca métodos separados
import time # Cria timer

while True:
    terminal.menu_inicial()
    try:
        r = int(input("Escolha uma das opções acima: "))

        if r == 1:
            terminal.menu_cadastro()
            r1 = int(input("Escolha uma das opções acima: "))
            if r1 == 1:
                metodos.cadastrar_cliente()
            elif r1 == 2:
                metodos.cadastrar_fornecedor()
            elif r1 == 3:
                metodos.cadastrar_produto()
            elif r1 == 4:
                print('')
            else:
                metodos.limpar_terminal()
        elif r == 2:
            terminal.menu_visualizar()
            r2 = int(input("Escolha uma das opções acima: "))
            if r2 == 1:
                metodos.visualizar_clientes()
            elif r2 == 2:
                metodos.visualizar_fornecedores()
            elif r2 == 3:
                metodos.visualizar_produtos()
            elif r2 == 4:
                print('')
            else:
                metodos.limpar_terminal()
        elif r == 3:
            terminal.sobre_o_candidato()
        elif r == 4:
            quit()
        else:
            metodos.limpar_terminal()
    except:
        metodos.limpar_terminal()