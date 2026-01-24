from funcoes import *
from classes import *
from time import sleep

enunciado("\033[33mPerguntas e Respostas\033[m".center(45))

jogador_atual = None
while True:
    if jogador_atual == None:
        escolha = menu3("Entrar na competição", "Ver Ranking", "Sair do jogo")
    else:
        escolha = menu3("Começar a competição", "Sua posição no ranking", "Sair do Jogo")
    if escolha == "3":
        limpar_tela()
        sleep(1)
        break
    elif escolha == "2":
        limpar_tela()
        ranking(jogador_atual)
        print("-" * 40)
        continue
    elif escolha == "1":
        if jogador_atual is not None:
            Jogo(jogador_atual)
            continue
        limpar_tela()
        enunciado("\033[35mConecte-se ou cadastre-se para jogar!\033[m".center(48))
        while True:
            escolha = menu2("Cadastrar", "Entrar")
            print("-" * 40)
            if escolha == "1":
                jogador_atual = cadastrar()
                sleep(1)
                limpar_tela()
                break
            elif escolha == "2":
                jogador_atual = login()
                sleep(1)
                limpar_tela()
                if jogador_atual:   
                    break           
                else:
                     print("\033[31mLogin inválido. Tente novamente.\033[m\n")
            else:
                enunciado("\033[31mOpção inválida. Tente novamente.\033[m\n")
        enunciado("\033[33mPerguntas e Respostas\033[m".center(45))
    else:
        enunciado("\033[31mOpção inválida. Tente novamente.\033[m")
enunciado(f"Carregando...") 
sleep(2) 
embaixo("Obrigado por jogar 1\033[33mPerguntas e Respostas!\033[m\nAté a próxima!")
