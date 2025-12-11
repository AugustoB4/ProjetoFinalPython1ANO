import json
import random
from classes import jogador # Importa apenas a classe jogador
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
        print("A senha precisa ter mais de 7 caracteres.")
        return False
    if not any(c.isalpha() for c in senha):
        print("A senha precisa ter pelo menos uma letra.")
        return False
    if not any(c.isnumeric() for c in senha):
        print("A senha precisa ter pelo menos um número.")
        return False
    return True

def cadastrar():
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)
    while True:
        nome = input("Digite seu nome de usuário: ").strip()
        nome_existente = False
        for usuario in dados["jogadores"]:
            if nome == usuario["nome"]:
                nome_existente = True
                break
        if nome_existente:
            print("Nome de Usuário já existente! Por favor, escolha outro.")
        else:
            break
    while True:
        senha = input("Digite sua senha: ").strip()
        if valida_senha(senha):
            break
    novo_jogador = jogador(nome, senha)
    dados["jogadores"].append({
        "nome": novo_jogador.nome,
        "senha": novo_jogador.senha,
        "dinheiro": 0,
    })
    with open(JOGADORES_PATH, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        sleep(0.5)
    enunciado(f"Jogador {nome} cadastrado com sucesso!")

def login():
    while True:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()
        with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)      
        for jogador_data in dados["jogadores"]:
            if jogador_data["nome"] == nome and jogador_data["senha"] == senha:
                jogador_atual = jogador(nome, senha, jogador_data["dinheiro"]) 
                emcima(f"Bem-vindo de volta, {nome}!")
                return jogador_atual
        emcima("Nome de usuário ou senha incorretos. Tente novamente.")
        return None 

#Jogo
def ranking():
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)
    jogadores_ordenados = sorted(dados["jogadores"], key=lambda x: x["dinheiro"], reverse=True)
    enunciado("Ranking dos Jogadores")
    sleep(0.5)
    for idx, jogador_data in enumerate(jogadores_ordenados, start=1):
        print(f" > {idx}. {jogador_data['nome']}", f" Dinheiro: R${jogador_data['dinheiro']:.2f}") 
        sleep(0.5)
    print("-" * 40)


def salvar_progresso(jogador_atual):
    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)  
    encontrado = False
    for jog in dados["jogadores"]:
        if jog["nome"] == jogador_atual.nome and jog["senha"] == jogador_atual.senha:
            jog["dinheiro"] = jogador_atual.saldo 
            encontrado = True
            break
    if encontrado:
        with open(JOGADORES_PATH, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

def Jogo(jogador_atual):
    print("Responda às perguntas e acumule pontos!\n",">Quanto mais pontos, mais perto do milhão.\n", "Boa sorte!")
    enunciado("Iniciando a competição...")
    sleep(0.5)
    dinheiro = jogador_atual.saldo
    contPerg = 0

    #Para escolher as perguntas
    while True:
        with open(PERGUNTAS_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)
        if not dados["conteudo"]:
            enunciado("Não há mais perguntas disponíveis!")
            break
        area = random.choice(dados["conteudo"])
        if not area["perguntas"]:
            continue 
        pergunta_data = random.choice(area["perguntas"])
        alternativas = pergunta_data["respostas"]
        correta = pergunta_data["correta"]

        #Esse é o jogo em si
        print(f"Tema: {area['area']}")
        print(pergunta_data["pergunta"])
        for alt in alternativas:
            sleep(0.2)
            print (">", alt)
        while True:
            resposta = input("Escolha a alternativa correta (A, B, C, D): ").strip().upper()
            if resposta in ["A", "B", "C", "D"]:
                break
            print("Insira uma resposta válida (A, B, C ou D).")

        if resposta == correta:
            sleep(0.5)
            enunciado("Resposta correta!")
            dinheiro += 1000 
        else:
            sleep(0.5)
            enunciado(f"Resposta incorreta! A resposta correta era {correta}.")
            dinheiro = dinheiro / 2 
        contPerg += 1
        print(f"Dinheiro atual: R${dinheiro:.2f}")
        if contPerg == 5:
            jogador_atual.saldo = dinheiro 
            salvar_progresso(jogador_atual) 
            print(f"\nVocê terminou esta rodada com R${jogador_atual.saldo:.2f}")
            escolha = menu2("Voltar ao menu inicial", "Começar outra partida")
            if escolha == "1":
                return 
            elif escolha == "2":
                enunciado("Iniciando nova partida...")
                contPerg = 0
            else:
                enunciado("Opção inválida. Voltando ao menu inicial.")
                return                
        sleep(1) 
    jogador_atual.saldo = dinheiro
    salvar_progresso(jogador_atual)
    enunciado(f"Fim da competição! Você agora está com R${jogador_atual.saldo:.2f}.")
    return