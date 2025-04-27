import metodos

def menu_inicial():
    metodos.limpar_terminal()
    print(
        '----Menu principal----\n'
        '\n'
        '[1]Menu de cadastro\n'
        '[2]Menu de visualização\n'
        '[3]Menu de modificação\n'
        '[4]Menu de remoção\n'
        '[5]Sobre o candidato\n'
        '[6]Sair\n'
        '\n'
    )

def menu_cadastro():
    metodos.limpar_terminal()
    print(
        '----Menu de cadastro----\n'
        '\n'
        '[1]Cadastrar cliente\n'
        '[2]Cadastrar fornecedor\n'
        '[3]Cadastrar produto\n'
        '[4]Voltar\n'
        '\n'
    )

def menu_visualizar():
    metodos.limpar_terminal()
    print(
        '----Menu de visualização----\n'
        '\n'
        '[1]Visualizar clientes\n'
        '[2]Visualizar fornecedores\n'
        '[3]Visualizar estoque\n'
        '[4]Voltar\n'
        '\n'
    )

def menu_modificacao():
    metodos.limpar_terminal()
    print(
        '----Menu de modificação----\n'
        '\n'
        '[1]Modificar cliente\n'
        '[2]Modificar fornecedor\n'
        '[3]Modificar produto\n'
        '[4]Voltar\n'
        '\n'
    )

def menu_remocao():
    metodos.limpar_terminal()
    print(
        '----Menu de remoção----\n'
        '\n'
        '[1]Remover cliente\n'
        '[2]Remover fornecedor\n'
        '[3]Remover produto\n'
        '[4]Voltar\n'
        '\n'
    )

def adicionando_cliente():
    print('----Cadastrando cliente----\n' \
    '\n')

def adicionando_fornecedor():
    print('----Cadastrando Fornecedor----\n' \
    '\n')

def adicionando_produto():
    print('----Cadastrando Produto----\n' \
    '\n')

def sobre_o_candidato():
    metodos.limpar_terminal()
    print(
        'Olá, meu nome é Kayky Carvalho. :)\n' \
        '\n'
        'Foi um prazer poder realizar este teste, ' \
        'agradeço pela oportunidade e caso queira conhecer mais sobre mim,\n' \
        'sinta-se a vontade para clicar em um dos links abaixo ou entrar em contato.\n'
        '\n'
        '- LinkedIn: https://www.linkedin.com/in/kayky-carvalho-/\n' \
        '- GitHub: https://github.com/KaykyCarvalho\n'
        '\n'
        '- Email: kayky.carvalho.cc@gmail.com\n' \
        '- Telefone: (11) 96039-6594\n'
        '- Whatsapp: https://api.whatsapp.com/send?phone=\n' \
        '\n'
    )
    input("Pressione Enter para voltar ao menu principal.")
    
