import json
import random 


with open("perguntas.json", "r", encoding="utf-8") as f:
    conteudo = json.load(f)
    def perguntar_aleatoria():
        pergunta = random.choice(conteudo["perguntas"])
        correta = pergunta["resposta_correta"]
        opcoes = pergunta["opcoes"]
        print(pergunta)
    print(perguntar_aleatoria())

            
    




        

