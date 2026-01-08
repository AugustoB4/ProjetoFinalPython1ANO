from funcoes import *
from classes import *
from time import sleep

enunciado("\033[33mShow do Milhão\033[m".center(45))

jogador_atual = None
while True:
    menu3("Entrar na competição", "Ver Ranking", "Sair do jogo")
    opcao_menu3 = int(input("Selecione uma opção: "))
    if opcao_menu3 == 3:
        sleep(1)
        break
    elif opcao_menu3 == 2:
        ranking()
        input("Pressione ENTER para voltar ao menu...")
        print("-" * 40)
        continue
    elif opcao_menu3 == 1:
        if jogador_atual is None:
            enunciado("É preciso estar cadastrado para entrar na competição.")
            menu2("Cadastrar","Entrar")
            opcao_menu2 = int(input("Selecione uma opção: "))
            if opcao_menu2 == 1:
                cadastrar()
                print("-" * 40)
            if opcao_menu2 == 2:
                login()
                print("-" * 40)
        if jogador_atual is not None:
            
                
                       

enunciado(f"Carregando...") 
sleep(2) 
enunciado("Obrigado por jogar o Show do Milhão!\nAté a próxima!")