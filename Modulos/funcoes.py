import json
import random
from classes import *

with open("perguntas.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)
def pergunta_aleatoria():
    area = random.choice(conteudo["conteudo"])
    pergunta = random.choice(area["perguntas"])
    print(f"Área: {area['area']}")
    print(f"Pergunta: {pergunta['pergunta']}")
    for resposta in pergunta["respostas"]:
        print(resposta)
    return pergunta["correta"]
    correta = pergunta_aleatoria()

def enunciado(texto):
    print("-" * 40)
    print(texto)
    print("-" * 40)

def menu3(Opc1, Opc2, Opc3):
    print("1.", Opc1)
    print("2.", Opc2)
    print("3.", Opc3)
    escolha = input("Escolha uma opção: ")
    return escolha

def menu2(Opc1, Opc2):
    print("1.", Opc1)
    print("2.", Opc2)
    escolha = input("Escolha uma opção: ")
    return escolha

def cadastrar():
    usuario = input("Crie seu nome de usuário: ")
    senha = input("Crie sua senha: ")
    jog = jogador(usuario, senha, 0, 0)
    with open("jogadores.json", "a", encoding="utf-8") as f:
        json.dumps(jog.__dict__)
    print("Cadastro realizado com sucesso!")

def login():
    usuario = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    jog = jogador(usuario, senha)
    with open("jogadores.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        for usuario_encontrado in dados:
            while usuario_encontrado["nome"] != jog.nome or usuario_encontrado["senha"] != jog.senha:
                print("Nome de usuário ou senha incorretos. Tente novamente.")
                usuario = input("Digite seu nome de usuário: ")
                senha = input("Digite sua senha: ")
                jog = jogador(usuario, senha)   
                if usuario_encontrado["nome"] == jog.nome and usuario_encontrado["senha"] == jog.senha:
                    print("Login realizado com sucesso!")
                    return usuario_encontrado

            
    




        

