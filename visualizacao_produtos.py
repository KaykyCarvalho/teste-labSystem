from prettytable import PrettyTable

def tabela_formata(resultados):
    if not resultados:
        print("Nenhum produto cadastrado.")
        return

    tabela = PrettyTable()
    tabela.field_names = ["ID", "NOME", "DATA_CADASTRO", "DESCRIÇÃO", "NOME_USUÁRIO", "QUANTIDADE", "VALOR"]

    for resultado in resultados:
        tabela.add_row(resultado)

    return tabela