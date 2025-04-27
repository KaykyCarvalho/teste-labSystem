from prettytable import PrettyTable

def tabela_formata(resultados):
    if not resultados:
        print("Nenhum cliente cadastrado.")
        return

    tabela = PrettyTable()
    tabela.field_names = ["ID", "NOME", "EMAIL", "DATA_CADASTRO",]

    for resultado in resultados:
        tabela.add_row(resultado)

    return tabela