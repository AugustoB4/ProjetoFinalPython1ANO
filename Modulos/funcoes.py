import json
import random
from classes import jogador
from pathlib import Path
from time import sleep

Path("Data").mkdir(exist_ok=True)
JOGADORES_PATH = "Data/jogadores.json"
PERGUNTAS_PATH = "Data/perguntas.json"

#Detalhes 
def enunciado(texto):
    print("-" * 40)
    print(texto)
    print("-" * 40)
    sleep(0.5)

def emcima(texto): 
    print("-" * 40)
    print(texto)
    sleep(0.5)

def embaixo(texto):
    print(texto)
    sleep(0.5)
    print("-" * 40)

def voltar_menu():
    enunciado("Voltando ao menu principal...")

#Menus
def menu3(Opc1, Opc2, Opc3):
    print("1.", Opc1)
    sleep(0.2)
    print("2.", Opc2)
    sleep(0.2)
    print("3.", Opc3)
    sleep(0.2)
    escolha = input("Escolha uma opção: ")
    return escolha

def menu2(Opc1, Opc2):
    print("1.", Opc1)
    sleep(0.2)
    print("2.", Opc2)
    sleep(0.2)
    escolha = input("Escolha uma opção: ")
    return escolha

#Usuario
def valida_senha(senha):
    if len(senha) < 8:
        enunciado("\033[31mA senha precisa ter mais de 7 caracteres.\033[m")
        return False
    if not any(c.isalpha() for c in senha):
        enunciado("\033[31mA senha precisa ter pelo menos uma letra.\033[m")
        return False
    if not any(c.isnumeric() for c in senha):
        enunciado("\033[31mA senha precisa ter pelo menos um número.\033[m")
        return False
    return True

def cadastrar():
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)
    while True:
        nome = input("Crie seu nome de usuário: ").strip()
        nome_existente = False
        for usuario in dados["jogadores"]:
            if nome == usuario["nome"]:
                nome_existente = True
                break
        if nome_existente:
            enunciado("\033[32mNome de Usuário já existente! Escolha outro.\033[m")
        else:
            break
    while True:
        senha = input("Crie uma senha: ").strip()
        if valida_senha(senha):
            break
    novo_jogador = jogador(nome, senha)
    dados["jogadores"].append({
        "nome": novo_jogador.nome,
        "senha": novo_jogador.senha,
        "pontuacao": 0,
    })
    with open(JOGADORES_PATH, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        sleep(0.5)
    enunciado(f"Jogador {nome} cadastrado com sucesso!")
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)      
    for jogador_data in dados["jogadores"]:
        if jogador_data["nome"] == nome and jogador_data["senha"] == senha:
            jogador_atual = jogador(nome, senha, jogador_data["pontuacao"]) 
            emcima(f"Seja bem-vindo(a), {nome}!")
            return jogador_atual

def login():
    while True:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()
        with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)      
        for jogador_data in dados["jogadores"]:
            if jogador_data["nome"] == nome and jogador_data["senha"] == senha:
                jogador_atual = jogador(nome, senha, jogador_data["pontuacao"]) 
                emcima(f"Bem-vindo de volta, {nome}!")
                return jogador_atual
        enunciado("\033[31mNome de usuário ou senha incorretos. Tente novamente.\033[m")


#Funções do jogo
def ranking():
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)
    jogadores_ordenados = sorted(dados["jogadores"], key=lambda x: x["pontuacao"], reverse=True)
    enunciado("\033[34mRanking dos Jogadores\033[m".center(46))
    sleep(0.5)
    for i, jogador_data in enumerate(jogadores_ordenados, start=1):
        print(f" > {i}. {jogador_data['nome']}", f" Pontuação {jogador_data['pontuacao']:.0f}") 
        sleep(0.2)
    print("-" * 40)


def salvar_progresso(jogador_atual):
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)  
    encontrado = False
    for jog in dados["jogadores"]:
        if jog["nome"] == jogador_atual.nome and jog["senha"] == jogador_atual.senha:
            jog["pontuacao"] = jogador_atual.saldo 
            encontrado = True
            break
    if encontrado:
        with open(JOGADORES_PATH, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            encontrado = True

'''def escolher_pergunta():
    with open(PERGUNTAS_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)
    area = random.choice(dados["conteudo"]) 
    perguntas_usadas = []
    pergunta_sorteada = random.choice(area["perguntas"])
    if pergunta_sorteada in perguntas_usadas:
        pergunta_sorteada = random.choice(area["perguntas"])
    else:
        dificuldade = pergunta_sorteada["dificuldade"]
        alternativas = pergunta_sorteada["respostas"]
        correta = pergunta_sorteada["correta"]
        perguntas_usadas.append(pergunta_sorteada)'''

#Jogo
def Jogo(jogador_atual):
    enunciado("\033[36mSeleção\033[m".center(44))
    QuanPerg = 0

    #Seleção da quantidade de perguntas
    while True:
        QuanPerg = input("Quantas perguntas deseja responder? [MIN:5 / MAX:20] ")
        if not QuanPerg.isdigit():
            enunciado("\033[31mInsira um número válido.\033[m")
            continue
        QuanPerg = int(QuanPerg)
        if 5 <= QuanPerg <= 20:
            break
        else:
            enunciado("\033[31mEscolha um número entre 5 e 20.\033[m")

    emcima("Processando...")
    sleep(0.5)
    enunciado("Responda às perguntas corretamente e ganhe pontos!\nQuanto mais pontos, maior seu ranking.\nBoa sorte!")
    sleep(0.5)
    embaixo("Iniciando a competição...")
    sleep(1)
    

    #Controle
    pontuacao = jogador_atual.saldo
    contPerg = 0
    acertos = 0
    erros = 0
    perguntas_usadas = []
    with open(PERGUNTAS_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)

    while True:
        contPerg += 1
    #Para escolher as perguntas
        
        area = random.choice(dados["conteudo"]) 
        pergunta_sorteada = random.choice(area["perguntas"])
        while pergunta_sorteada in perguntas_usadas:
            pergunta_sorteada = random.choice(area["perguntas"])
        else:
            dificuldade = pergunta_sorteada["dificuldade"]
            alternativas = pergunta_sorteada["respostas"]
            correta = pergunta_sorteada["correta"]
            perguntas_usadas.append(pergunta_sorteada)
        
            '''escolher_pergunta()'''

        #Agora é o jogo em si
            if dificuldade == "fácil":
                print(f"Dificuldade: \033[32m{dificuldade}\033[m")
            elif dificuldade == "médio":
                print(f"Dificuldade: \033[33m{dificuldade}\033[m")
            elif dificuldade == "difícil":
                print(f"Dificuldade: \033[31m{dificuldade}\033[m")
            
            print(f"Tema: {area['area']}")
            print(pergunta_sorteada["pergunta"])
            for alt in alternativas:
                sleep(0.2)
                print (">", alt)
            while True:
                resposta = input("Escolha a alternativa correta (A, B, C, D): ").strip().upper()
                if resposta in ["A", "B", "C", "D"]:
                    break
                enunciado("\033[31mInsira uma resposta válida (A, B, C ou D).\033[m")

            if resposta == correta:
                acertos += 1
                sleep(0.5)
                enunciado("\033[32mResposta correta!\033[m")
                if dificuldade == "fácil":
                    pontuacao += 10
                elif dificuldade == "médio":
                    pontuacao += 25
                elif dificuldade == "difícil":
                    pontuacao += 50
            else:
                erros += 1
                sleep(0.5)
                enunciado(f"\033[31mResposta incorreta!\033[m A resposta correta era \033[32m{correta}\033[m. ")
                if dificuldade == "fácil":
                    if pontuacao > 10:
                        pontuacao -= 10
                    else:
                        pontuacao -= (pontuacao * 0.5)
                elif dificuldade == "médio":
                    if pontuacao > 15:
                        pontuacao -= 15
                    else:
                        pontuacao -= (pontuacao * 0.5)
                elif dificuldade == "difícil":
                    if pontuacao > 30:
                        pontuacao -= 30
                    else:
                        pontuacao -= (pontuacao * 0.5)
                elif pontuacao < 1:
                    pontuacao = 1
            print(f"Sua pontuação atual: \033[4m{pontuacao:.0f}\033[m")
            print("-" * 40)
            if QuanPerg == QuanPerg // 2:
                while escolha not in ["1", "2"]:
                    escolha = menu2("Continuar a competição", "Desistir")
                    if escolha == "1":
                        continue
                    elif escolha == "2":
                        break
                    elif escolha not in ["1", "2"]:
                        print("\033[31mSelecione uma opção válida\033[m")
        if contPerg == QuanPerg:
            jogador_atual.saldo = pontuacao 
            salvar_progresso(jogador_atual) 
            print(f"Você terminou esta rodada com \033[4m{jogador_atual.saldo:.0f}\033[m pontos!")
            print("Com um total de:")
            if acertos > 1:
                print(f"-> \033[32m{acertos}\033[m acertos;")
            if acertos == 1:
                print(f"-> \033[32m{acertos}\033[m acerto;")
            if erros > 1:
                print(f"-> \033[31m{erros}\033[m erros.")
            if erros == 1:
                print(f"-> \033[31m{erros}\033[m erro.")
            print("-" * 40)

            escolha = None
            while escolha not in ["1", "2"]:
                escolha = menu2("Voltar ao menu inicial", "Começar outra partida")
                if escolha == "1":
                    print("-" * 40)
                    return 
                elif escolha == "2":
                    enunciado("Iniciando nova partida...")
                    sleep(1)
                    contPerg = 0
                    perguntas_usadas.clear()
                    continue
                elif escolha not in ["1", "2"]:
                    enunciado("\033[31mOpção inválida.\033[m")
            
                          