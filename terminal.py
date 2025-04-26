import time
import os
import metodos

def menu_inicial():
    metodos.limpar_terminal()
    print('----Menu principal----\n'
    '\n'
    '[1]Cadastrar cliente\n'
    '[2]Cadastrar fornecedor\n'
    '[3]Cadastrar produto\n'
    '[4]Visualizar estoque\n'
    '[5]Sobre o candidato\n'
    '[6]Sair\n'
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
    
