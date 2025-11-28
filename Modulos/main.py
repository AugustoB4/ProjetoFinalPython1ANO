from Modulos.funcoes import *
from Modulos.classes import *
'''
    print("1. Entrar na competição")
    print("2. Ver Ranking")
    print("3. Sair do jogo")
    escolha = input("Escolha uma opção: ")
    return escolha'''

enunciado("\033[33mShow do Milhão\033[m".center(45))
while True:
    menu3( "Entrar na competição", "Ver Ranking", "Sair do jogo")
    escolha = menu()
    if escolha == "1":
        enunciado("Conecte-se ou cadastre-se para jogar!")
        menu2("Caddastrar", "Entrar")
        if escolha == "1":
            cadastrar()


    





