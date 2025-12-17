# ================== IMPORTAÇÕES ==================

import customtkinter as ctk
import json
import random

from classes import jogador
from funcoes import (
    JOGADORES_PATH,
    PERGUNTAS_PATH,
    salvar_progresso,
    valida_senha
)

# ================== CONFIGURAÇÃO DA JANELA ==================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Show do Milhão")
app.geometry("800x600")

jogador_atual = None
dinheiro = 0

# ================== FUNÇÃO PARA LIMPAR TELA ==================

def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()

# ================== TELA MENU ==================

def tela_menu():
    limpar_tela()

    ctk.CTkLabel(
        app,
        text="SHOW DO MILHÃO",
        font=("Arial", 30, "bold")
    ).pack(pady=40)

    ctk.CTkButton(app, text="Login", width=200, command=tela_login).pack(pady=10)
    ctk.CTkButton(app, text="Cadastrar", width=200, command=tela_cadastro).pack(pady=10)
    ctk.CTkButton(app, text="Ranking", width=200, command=tela_ranking).pack(pady=10)
    ctk.CTkButton(app, text="Sair", width=200, command=app.destroy).pack(pady=10)

# ================== LOGIN ==================

def tela_login():
    limpar_tela()

    ctk.CTkLabel(app, text="Login", font=("Arial", 24, "bold")).pack(pady=20)

    entrada_nome = ctk.CTkEntry(app, placeholder_text="Usuário")
    entrada_nome.pack(pady=10)

    entrada_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*")
    entrada_senha.pack(pady=10)

    aviso = ctk.CTkLabel(app, text="")
    aviso.pack(pady=10)

    def fazer_login():
        global jogador_atual, dinheiro

        nome = entrada_nome.get()
        senha = entrada_senha.get()

        with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for j in dados["jogadores"]:
            if j["nome"] == nome and j["senha"] == senha:
                jogador_atual = jogador(nome, senha, j["dinheiro"])
                dinheiro = jogador_atual.saldo
                tela_jogo()
                return

        aviso.configure(text="Usuário ou senha incorretos")

    ctk.CTkButton(app, text="Entrar", command=fazer_login).pack(pady=10)
    ctk.CTkButton(app, text="Voltar", command=tela_menu).pack(pady=10)

# ================== CADASTRO ==================

def tela_cadastro():
    limpar_tela()

    ctk.CTkLabel(app, text="Cadastro", font=("Arial", 24, "bold")).pack(pady=20)

    entrada_nome = ctk.CTkEntry(app, placeholder_text="Usuário")
    entrada_nome.pack(pady=10)

    entrada_senha = ctk.CTkEntry(app, placeholder_text="Senha")
    entrada_senha.pack(pady=10)

    aviso = ctk.CTkLabel(app, text="")
    aviso.pack(pady=10)

    def cadastrar_usuario():
        nome = entrada_nome.get()
        senha = entrada_senha.get()

        if not valida_senha(senha):
            aviso.configure(text="Senha inválida (mín. 8, letra e número)")
            return

        with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for j in dados["jogadores"]:
            if j["nome"] == nome:
                aviso.configure(text="Usuário já existe")
                return

        dados["jogadores"].append({
            "nome": nome,
            "senha": senha,
            "dinheiro": 0
        })

        with open(JOGADORES_PATH, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        aviso.configure(text="Cadastro realizado com sucesso!")

    ctk.CTkButton(app, text="Cadastrar", command=cadastrar_usuario).pack(pady=10)
    ctk.CTkButton(app, text="Voltar", command=tela_menu).pack(pady=10)

# ================== RANKING ==================

def tela_ranking():
    limpar_tela()

    ctk.CTkLabel(app, text="Ranking", font=("Arial", 24, "bold")).pack(pady=20)

    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)

    ranking = sorted(dados["jogadores"], key=lambda x: x["dinheiro"], reverse=True)

    for i, j in enumerate(ranking, start=1):
        ctk.CTkLabel(
            app,
            text=f"{i}. {j['nome']} - R${j['dinheiro']:.2f}",
            font=("Arial", 16)
        ).pack(pady=5)

    ctk.CTkButton(app, text="Voltar", command=tela_menu).pack(pady=20)

# ================== JOGO ==================

def tela_jogo():
    limpar_tela()
    global dinheiro

    with open(PERGUNTAS_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)

    area = random.choice(dados["conteudo"])
    pergunta = random.choice(area["perguntas"])
    correta = pergunta["correta"]

    # ----- TOPO -----
    topo = ctk.CTkFrame(app)
    topo.pack(fill="x", pady=10)

    ctk.CTkLabel(
        topo,
        text=f"Jogador: {jogador_atual.nome}",
        font=("Arial", 14, "bold")
    ).pack(side="left", padx=20)

    saldo_label = ctk.CTkLabel(
        topo,
        text=f"Saldo: R${dinheiro:.2f}",
        font=("Arial", 14, "bold")
    )
    saldo_label.pack(side="right", padx=20)

    # ----- CONTEÚDO -----
    conteudo = ctk.CTkFrame(app)
    conteudo.pack(padx=30, pady=20, fill="both", expand=True)

    ctk.CTkLabel(
        conteudo,
        text=f"Tema: {area['area']}",
        font=("Arial", 12, "italic")
    ).pack(pady=5)

    ctk.CTkLabel(
        conteudo,
        text=pergunta["pergunta"],
        font=("Arial", 20, "bold"),
        wraplength=650,
        justify="center"
    ).pack(pady=20)

    resultado = ctk.CTkLabel(conteudo, text="", font=("Arial", 16))
    resultado.pack(pady=10)

    def responder(letra):
        global dinheiro

        if letra == correta:
            dinheiro += 1000
            resultado.configure(text="Resposta correta!")
        else:
            dinheiro /= 2
            resultado.configure(text=f"Resposta errada! Correta: {correta}")

        jogador_atual.saldo = dinheiro
        salvar_progresso(jogador_atual)
        saldo_label.configure(text=f"Saldo: R${dinheiro:.2f}")

    for alt in pergunta["respostas"]:
        letra = alt[0]
        ctk.CTkButton(
            conteudo,
            text=alt,
            width=450,
            height=40,
            font=("Arial", 15),
            command=lambda l=letra: responder(l)
        ).pack(pady=6)

    # ----- RODAPÉ -----
    rodape = ctk.CTkFrame(app)
    rodape.pack(pady=15)

    ctk.CTkButton(rodape, text="Próxima pergunta", width=180, command=tela_jogo)\
        .pack(side="left", padx=10)

    ctk.CTkButton(rodape, text="Parar o jogo", width=180, command=tela_menu)\
        .pack(side="right", padx=10)

# ================== INICIAR ==================

tela_menu()
app.mainloop()