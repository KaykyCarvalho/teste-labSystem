import terminal # mostra as telas no terminal
import metodos # Busca métodos separados

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
            terminal.menu_modificacao()
            r3 = int(input("Escolha uma das opções acima: "))
            if r3 == 1:
                metodos.modificar_cliente()
            elif r3 == 2:
                metodos.modificar_fornecedor()
            elif r3 == 3:
                metodos.modificar_produto()
            elif r3 == 4:
                print('')
            else:
                metodos.limpar_terminal()
        elif r == 4:
            terminal.menu_remocao()
            r4 = int(input("Escolha uma das opções acima: "))
            if r4 == 1:
                metodos.remover_cliente()
            elif r4 == 2:
                metodos.remover_fornecedor()
            elif r4 == 3:
                metodos.remover_produto()
            elif r4 == 4:
                print('')
            else:
                metodos.limpar_terminal()
        elif r == 5:
            terminal.sobre_o_candidato()
        elif r == 6:
            quit()
        else:
            metodos.limpar_terminal()
    except:
        metodos.limpar_terminal()