import json
import random
from classes import *
from pathlib import Path
from time import sleep

def enunciado(texto):
    print("-" * 40)
    print(texto)
    print("-" * 40)
    sleep(0.5)

def menu3(Opc1, Opc2, Opc3):
    print("1.", Opc1)
    sleep(0.2)
    print("2.", Opc2)
    sleep(0.2)
    print("3.", Opc3)
    sleep(0.2)
    escolha = input("Escolha uma opção: ")
    return escolha
sleep(0.5)

def menu2(Opc1, Opc2):
    print("1.", Opc1)
    sleep(0.2)
    print("2.", Opc2)
    sleep(0.2)
    escolha = input("Escolha uma opção: ")
    return escolha
sleep(0.5)

import json

def cadastrar():
    nome = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()
    novo_jogador = jogador(nome, senha)
    with open("Data/jogadores.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    dados["jogadores"].append({
        "nome": novo_jogador.nome,
        "senha": novo_jogador.senha,
        "pontos": 0,
        "dinheiro": 0,
        "rank": "Iniciante"
    })
    with open("Data/jogadores.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
        sleep(0.5)
    enunciado(f"Jogador {nome} cadastrado com sucesso!")

def login():
    while True:
        nome = input("Digite seu nome de usuário: ").strip()
        senha = input("Digite sua senha: ").strip()
        with open("Data/jogadores.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
        for jogador_data in dados["jogadores"]:
            if jogador_data["nome"] == nome and jogador_data["senha"] == senha:
                enunciado(f"Bem-vindo de volta, {nome}!")
                jogador_atual = jogador(nome, senha)
                jogador_atual.pontuação(jogador_data["pontos"], jogador_data["dinheiro"], jogador_data["rank"])
                return jogador_atual
        enunciado("Nome de usuário ou senha incorretos. Tente novamente.")
        sleep(0.5)
            
def ranking():
    with open("Data/jogadores.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    jogadores_ordenados = sorted(dados["jogadores"], key=lambda x: x["pontos"], reverse=True)
    enunciado("Ranking dos Jogadores")
    sleep(0.5)
    for idx, jogador_data in enumerate(jogadores_ordenados, start=1):
        print(f" > {idx}. {jogador_data['nome']}", f"- Pontos: {jogador_data['pontos']}, Dinheiro: {jogador_data['dinheiro']}, Rank: {jogador_data['rank']}")
        sleep(0.5)
    print("-" * 40)

def voltar_menu():
    enunciado("Voltando ao menu principal...")










        

