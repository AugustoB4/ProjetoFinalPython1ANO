from funcoes import *
from classes import *
from time import sleep

enunciado("\033[33mPerguntas e Respostas\033[m".center(45))

jogador_atual = None
while True:
    escolha = menu3("Entrar na competição", "Ver Ranking", "Sair do jogo")
    if escolha == "3":
        sleep(1)
        break
    elif escolha == "2":
        ranking()
        input("Pressione ENTER para voltar ao menu...")
        print("-" * 40)
        continue
    elif escolha == "1":
        if jogador_atual is not None:
            Jogo(jogador_atual)
            continue
        enunciado("\033[35mConecte-se ou cadastre-se para jogar!\033[m".center(48))
        while True:
            escolha = menu2("Cadastrar", "Entrar")
            print("-" * 40)
            if escolha == "1":
                jogador_atual = cadastrar()
                print("\nCadastro concluído!")
                break
            elif escolha == "2":
                jogador_atual = login()
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
embaixo("Obrigado por jogar o \033[33mPerguntas e Respostas!\033[m\nAté a próxima!")