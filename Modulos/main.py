from funcoes import *
from classes import *
from time import sleep

jogador_atual = None
enunciado("\033[33mShow do Milhão\033[m".center(45))

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
        if jogador_atual:
            Jogo(jogador_atual)
            continue
        enunciado("Conecte-se ou cadastre-se para jogar!")
        while True:
            escolha_login = menu2("Cadastrar", "Entrar")
            if escolha_login == "1":
                cadastrar()
                print("\nCadastro concluído! Agora faça login.\n")
            elif escolha_login == "2":
                jogador_atual = login()
                if jogador_atual:   
                    break           
                else:
                    print("Usuário/senha incorretos! Tente novamente.\n")
            else:
                print("Opção inválida.")
        enunciado("\033[33mShow do Milhão\033[m".center(45))
        Jogo(jogador_atual)
        continue 
    else:
        print("Opção inválida. Tente novamente.")   
enunciado(f"Carregando...") 
sleep(2) 
enunciado("Obrigado por jogar o Show do Milhão!\nAté a próxima!")