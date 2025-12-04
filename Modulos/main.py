from funcoes import *
from classes import *
from time import sleep
'''
    print("1. Entrar na competição")
    print("2. Ver Ranking")
    print("3. Sair do jogo")
    escolha = input("Escolha uma opção: ")
    return escolha'''

resp = "s"
enunciado("\033[33mShow do Milhão\033[m".center(45))
while True:
    escolha = menu3( "Entrar na competição", "Ver Ranking", "Sair do jogo")
    if escolha == "1":
        enunciado("Conecte-se ou cadastre-se para jogar!")
        escolha = menu2("Cadastrar", "Entrar")
        if escolha == "1":
            cadastrar()
            sleep(0.5)

            login()
        if escolha == "2":
            login()
    if escolha == "2":
        ranking()
    if escolha == "3":
        sleep(1)
        break
   
    enunciado("Bem-vindo ao Show do Milhão!\nResponda às perguntas e acumule pontos!\nQuanto mais pontos, mais perto do milhão.\nBoa sorte!")
    jogador_atual = login()

enunciado(f"Carregando...")
sleep(2)
enunciado("Obrigado por jogar o Show do Milhão!\nAté a próxima!")
    


    



    





