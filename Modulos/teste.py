from funcoes import *
import json
import random

Path("Data").mkdir(exist_ok=True)
Path("Data/jogadores").mkdir(exist_ok=True)

JOGADORES_PATH = "Data/jogadores.json"
PERGUNTAS_PATH_FACIL = "Data/perguntas/facil.json"
PERGUNTAS_PATH_MEDIO = "Data/perguntas/medio.json"
PERGUNTAS_PATH_DIFICIL = "Data/perguntas/dificil.json"
 

with open(PERGUNTAS_PATH_FACIL, "r", encoding="utf-8") as f:
    dados = json.load(f)
area = random.choice(dados["conteudo"]) 
pergunta_data = random.choice(area["perguntas"])
alternativas = pergunta_data["respostas"]
correta = pergunta_data["correta"]
print(area)
print(pergunta_data)
print(alternativas)
print(correta)