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

# ======================
# CONFIGURAÇÃO GLOBAL
# ======================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Show do Milhão")
app.geometry("900x700")

jogador_atual = None
dinheiro = 0


# ======================
# FUNÇÃO LIMPAR TELA
# ======================
def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()


# ======================
# TELA MENU
# ======================
def tela_menu():
    limpar_tela()

    container = ctk.CTkFrame(app, corner_radius=20)
    container.pack(expand=True, padx=60, pady=60)

    ctk.CTkLabel(
        container,
        text="SHOW DO MILHÃO",
        font=("Arial Black", 42)
    ).pack(pady=40)

    for texto, comando in [
        ("LOGIN", tela_login),
        ("CADASTRAR", tela_cadastro),
        ("RANKING", tela_ranking)
    ]:
        ctk.CTkButton(
            container,
            text=texto,
            width=320,
            height=60,
            font=("Arial", 20, "bold"),
            corner_radius=15,
            command=comando
        ).pack(pady=12)

    ctk.CTkButton(
        container,
        text="SAIR",
        width=320,
        height=60,
        font=("Arial", 20, "bold"),
        fg_color="#8b0000",
        hover_color="#a80000",
        corner_radius=15,
        command=app.destroy
    ).pack(pady=30)


# ======================
# LOGIN
# ======================
def tela_login():
    limpar_tela()

    card = ctk.CTkFrame(app, corner_radius=20)
    card.pack(expand=True, padx=80, pady=80)

    ctk.CTkLabel(card, text="Login", font=("Arial Black", 28)).pack(pady=20)

    entrada_nome = ctk.CTkEntry(card, placeholder_text="Usuário", width=300)
    entrada_nome.pack(pady=10)

    entrada_senha = ctk.CTkEntry(card, placeholder_text="Senha", show="*", width=300)
    entrada_senha.pack(pady=10)

    aviso = ctk.CTkLabel(card, text="")
    aviso.pack(pady=10)

    def fazer_login():
        global jogador_atual, dinheiro

        with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for j in dados["jogadores"]:
            if j["nome"] == entrada_nome.get() and j["senha"] == entrada_senha.get():
                jogador_atual = jogador(j["nome"], j["senha"], j["dinheiro"])
                dinheiro = jogador_atual.saldo
                tela_jogo()
                return

        aviso.configure(text="Usuário ou senha incorretos")

    ctk.CTkButton(card, text="Entrar", width=200, command=fazer_login).pack(pady=10)
    ctk.CTkButton(card, text="Voltar", width=200, command=tela_menu).pack(pady=10)


# ======================
# CADASTRO
# ======================
def tela_cadastro():
    limpar_tela()

    card = ctk.CTkFrame(app, corner_radius=20)
    card.pack(expand=True, padx=80, pady=80)

    ctk.CTkLabel(card, text="Cadastro", font=("Arial Black", 28)).pack(pady=20)

    entrada_nome = ctk.CTkEntry(card, placeholder_text="Usuário", width=300)
    entrada_nome.pack(pady=10)

    entrada_senha = ctk.CTkEntry(card, placeholder_text="Senha", width=300)
    entrada_senha.pack(pady=10)

    aviso = ctk.CTkLabel(card, text="")
    aviso.pack(pady=10)

    def cadastrar_usuario():
        if not valida_senha(entrada_senha.get()):
            aviso.configure(text="Senha inválida (mín. 8, letra e número)")
            return

        with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
            dados = json.load(f)

        for j in dados["jogadores"]:
            if j["nome"] == entrada_nome.get():
                aviso.configure(text="Usuário já existe")
                return

        dados["jogadores"].append({
            "nome": entrada_nome.get(),
            "senha": entrada_senha.get(),
            "dinheiro": 0
        })

        with open(JOGADORES_PATH, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        aviso.configure(text="Cadastro realizado com sucesso!")

    ctk.CTkButton(card, text="Cadastrar", width=200, command=cadastrar_usuario).pack(pady=10)
    ctk.CTkButton(card, text="Voltar", width=200, command=tela_menu).pack(pady=10)


# ======================
# RANKING
# ======================
def tela_ranking():
    limpar_tela()

    card = ctk.CTkFrame(app, corner_radius=20)
    card.pack(expand=True, padx=80, pady=80)

    ctk.CTkLabel(card, text="Ranking", font=("Arial Black", 28)).pack(pady=20)

    with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)

    ranking = sorted(dados["jogadores"], key=lambda x: x["dinheiro"], reverse=True)

    for i, j in enumerate(ranking, start=1):
        ctk.CTkLabel(
            card,
            text=f"{i}. {j['nome']} - R${j['dinheiro']:.2f}",
            font=("Arial", 16)
        ).pack(pady=6)

    ctk.CTkButton(card, text="Voltar", width=200, command=tela_menu).pack(pady=20)


# ======================
# JOGO
# ======================
def tela_jogo():
    limpar_tela()
    global dinheiro

    with open(PERGUNTAS_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)

    area = random.choice(dados["conteudo"])
    pergunta = random.choice(area["perguntas"])

    topo = ctk.CTkFrame(app)
    topo.pack(fill="x", padx=20, pady=10)

    ctk.CTkLabel(
        topo,
        text=f"Jogador: {jogador_atual.nome}",
        font=("Arial", 14, "bold")
    ).pack(side="left")

    saldo_label = ctk.CTkLabel(
        topo,
        text=f"Saldo: R${dinheiro:.2f}",
        font=("Arial", 14, "bold")
    )
    saldo_label.pack(side="right")

    card = ctk.CTkFrame(app, corner_radius=20)
    card.pack(expand=True, padx=40, pady=20)

    ctk.CTkLabel(
        card,
        text=f"Tema: {area['area']}",
        font=("Arial", 14, "italic")
    ).pack(pady=10)

    ctk.CTkLabel(
        card,
        text=pergunta["pergunta"],
        font=("Arial Black", 22),
        wraplength=700,
        justify="center"
    ).pack(pady=25)

    resultado = ctk.CTkLabel(card, text="", font=("Arial", 18))
    resultado.pack(pady=10)

    def responder(letra):
        global dinheiro
        if letra == pergunta["correta"]:
            dinheiro += 1000
            resultado.configure(text="Resposta correta!")
        else:
            dinheiro /= 2
            resultado.configure(text=f"Resposta errada! Correta: {pergunta['correta']}")

        jogador_atual.saldo = dinheiro
        salvar_progresso(jogador_atual)
        saldo_label.configure(text=f"Saldo: R${dinheiro:.2f}")

    for alt in pergunta["respostas"]:
        letra = alt[0]
        ctk.CTkButton(
            card,
            text=alt,
            width=650,
            height=60,
            font=("Arial", 18, "bold"),
            corner_radius=15,
            command=lambda l=letra: responder(l)
        ).pack(pady=8)

    rodape = ctk.CTkFrame(app)
    rodape.pack(pady=15)

    ctk.CTkButton(rodape, text="Próxima pergunta", width=200, command=tela_jogo).pack(side="left", padx=10)
    ctk.CTkButton(rodape, text="Parar o jogo", width=200, command=tela_menu).pack(side="right", padx=10)


# ======================
# INÍCIO
# ======================
tela_menu()
app.mainloop()