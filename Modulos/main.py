from funcoes import *
from classes import *
from time import sleep

enunciado("\033[33mShow do Milhão\033[m".center(45))

jogador_atual = None
while True:
    escolha = menu3("Entrar na competição", "Ver Ranking", "Sair do jogo")
    if escolha == "3":
        sleep(1)
        break
    elif escolha == "2":
        ranking()
        input("Pressione ENTER para voltar ao menu...")
        continue
    elif escolha == "1":
        if jogador_atual is not None:
            Jogo(jogador_atual)
            continue
        enunciado("Conecte-se ou cadastre-se para jogar!")
        while True:
            escolha = menu2("Cadastrar", "Entrar")
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
        enunciado("\033[33mShow do Milhão\033[m".center(45))
    else:
        enunciado("\033[31mOpção inválida. Tente novamente.\033[m")
enunciado(f"Carregando...") 
sleep(2) 
enunciado("Obrigado por jogar o Show do Milhão!\nAté a próxima!")