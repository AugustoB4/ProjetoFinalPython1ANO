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
app.title("Master of Knowledge")
app.geometry("900x750")

jogador_atual = None
pontuacao_total = 0 

COR_DOURADO = "#D4AF37"
COR_FUNDO_PAINEL = "#1e293b"
COR_BOTAO_PADRAO = "#3b82f6"

# Cores nítidas para feedback (Verde e Vermelho vivos)
VERDE_OK = "#22c55e"   
VERMELHO_ERRO = "#ef4444" 

def limpar_tela():
    for widget in app.winfo_children():
        widget.destroy()

# ======================
# TELAS DE ACESSO
# ======================
def tela_menu():
    limpar_tela()
    container = ctk.CTkFrame(app, corner_radius=25, fg_color="transparent")
    container.pack(expand=True)
    ctk.CTkLabel(container, text="MASTER OF\nKNOWLEDGE", font=("Georgia", 52, "bold"), text_color=COR_DOURADO).pack(pady=(0, 40))
    for t, c in [("LOGIN", tela_login), ("CADASTRO", tela_cadastro), ("RANKING", tela_ranking)]:
        ctk.CTkButton(container, text=t, width=320, height=55, font=("Arial", 18, "bold"), command=c).pack(pady=10)
    ctk.CTkButton(container, text="SAIR", width=320, height=55, fg_color="#7f1d1d", command=app.destroy).pack(pady=30)

def tela_login():
    limpar_tela()
    card = ctk.CTkFrame(app, corner_radius=20, fg_color=COR_FUNDO_PAINEL)
    card.pack(expand=True, padx=80, pady=80)
    ctk.CTkLabel(card, text="Acesso ao Sistema", font=("Arial Black", 26), text_color=COR_DOURADO).pack(pady=25)
    entrada_nome = ctk.CTkEntry(card, placeholder_text="Usuário", width=300)
    entrada_nome.pack(pady=10)
    entrada_senha = ctk.CTkEntry(card, placeholder_text="Senha", show="*", width=300)
    entrada_senha.pack(pady=10)
    
    def realizar_login():
        global jogador_atual, pontuacao_total
        try:
            with open(JOGADORES_PATH, "r", encoding="utf-8") as f:
                dados = json.load(f)
            for j in dados["jogadores"]:
                if j["nome"] == entrada_nome.get() and j["senha"] == entrada_senha.get():
                    jogador_atual = jogador(j["nome"], j["senha"], j.get("pontuacao", 0))
                    pontuacao_total = jogador_atual.saldo # Pega a pontuação salva
                    tela_jogo()
                    return
        except: pass
    ctk.CTkButton(card, text="Entrar", command=realizar_login).pack(pady=10)
    ctk.CTkButton(card, text="Voltar", fg_color="transparent", border_width=1, command=tela_menu).pack()

def tela_cadastro():
    limpar_tela()
    card = ctk.CTkFrame(app, corner_radius=20, fg_color=COR_FUNDO_PAINEL)
    card.pack(expand=True, padx=80, pady=80)
    ctk.CTkLabel(card, text="Novo Usuário", font=("Arial Black", 26), text_color=COR_DOURADO).pack(pady=25)
    entrada_nome = ctk.CTkEntry(card, placeholder_text="Usuário", width=300)
    entrada_nome.pack(pady=10)
    entrada_senha = ctk.CTkEntry(card, placeholder_text="Senha", width=300)
    entrada_senha.pack(pady=10)
    
    def salvar():
        with open(JOGADORES_PATH, "r", encoding="utf-8") as f: dados = json.load(f)
        dados["jogadores"].append({"nome": entrada_nome.get(), "senha": entrada_senha.get(), "pontuacao": 0})
        with open(JOGADORES_PATH, "w", encoding="utf-8") as f: json.dump(dados, f, indent=4)
        tela_menu()
    ctk.CTkButton(card, text="Cadastrar", command=salvar).pack(pady=10)
    ctk.CTkButton(card, text="Voltar", fg_color="transparent", border_width=1, command=tela_menu).pack()

# ======================
# RANKING
# ======================
def tela_ranking():
    limpar_tela()
    card = ctk.CTkFrame(app, corner_radius=20, fg_color=COR_FUNDO_PAINEL)
    card.pack(pady=20, padx=100, fill="both", expand=True)
    ctk.CTkLabel(card, text="RANKING", font=("Arial Black", 28), text_color=COR_DOURADO).pack(pady=15)
    lista = ctk.CTkScrollableFrame(card, fg_color="transparent", height=350)
    lista.pack(fill="both", expand=True, padx=20, pady=5)
    
    try:
        with open(JOGADORES_PATH, "r", encoding="utf-8") as f: dados = json.load(f)
        ranking_data = sorted(dados["jogadores"], key=lambda x: x.get("pontuacao", 0), reverse=True)
        for i, j in enumerate(ranking_data[:10], start=1):
            item = ctk.CTkFrame(lista, fg_color="#2d3748", height=35)
            item.pack(fill="x", pady=2)
            ctk.CTkLabel(item, text=f"{i}º {j['nome']}", font=("Arial", 14, "bold")).pack(side="left", padx=15)
            ctk.CTkLabel(item, text=f"{int(j.get('pontuacao',0))} pts", text_color=COR_DOURADO, font=("Arial", 14, "bold")).pack(side="right", padx=15)
    except: pass
    
    ctk.CTkButton(card, text="VOLTAR AO MENU", width=200, height=45, command=tela_menu).pack(pady=20)

# ======================
# JOGO (AJUSTADO: PONTOS E VISÃO)
# ======================
def tela_jogo():
    limpar_tela()
    global pontuacao_total
    with open(PERGUNTAS_PATH, "r", encoding="utf-8") as f: dados = json.load(f)

    area_obj = random.choice(dados["conteudo"])
    pergunta = random.choice(area_obj["perguntas"])
    dificuldade = pergunta.get("dificuldade", "fácil").lower()

    topo = ctk.CTkFrame(app, height=60, fg_color="#0f172a")
    topo.pack(fill="x")
    ctk.CTkLabel(topo, text=f"Mestre: {jogador_atual.nome}", font=("Arial", 14, "bold")).pack(side="left", padx=20)
    pontos_label = ctk.CTkLabel(topo, text=f"PONTOS: {int(pontuacao_total)}", font=("Arial Black", 20), text_color=COR_DOURADO)
    pontos_label.pack(side="right", padx=20)

    card = ctk.CTkFrame(app, corner_radius=20, fg_color=COR_FUNDO_PAINEL)
    card.pack(expand=True, padx=40, pady=20, fill="both")

    # Matéria e Nível
    ctk.CTkLabel(
        card, 
        text=f"{area_obj['area'].upper()} | DIFICULDADE: {dificuldade.upper()}", 
        font=("Arial", 18, "bold"), 
        text_color="#cbd5e1" 
    ).pack(pady=(25, 10))

    ctk.CTkLabel(card, text=pergunta["pergunta"], font=("Arial", 26, "bold"), wraplength=750).pack(pady=35)

    lista_botoes = {}
    def responder(letra_escolhida):
        global pontuacao_total
        # Bloqueia cliques múltiplos
        for b in lista_botoes.values(): b.configure(state="disabled")
        
        correta = pergunta["correta"]
        pontos_map = {"fácil": 10, "médio": 25, "média": 25, "difícil": 50}
        valor = pontos_map.get(dificuldade, 10)

        # Revela cores e coloca TEXTO PRETO
        for letra, botao in lista_botoes.items():
            if letra == correta:
                botao.configure(fg_color=VERDE_OK, text_color="black", font=("Arial", 18, "bold"))
            else:
                botao.configure(fg_color=VERMELHO_ERRO, text_color="black", font=("Arial", 18, "bold"))

        if letra_escolhida == correta:
            pontuacao_total += valor
        else:
            pontuacao_total = max(0, pontuacao_total - (valor / 2)) # Perde metade do valor da questão se errar
        
        jogador_atual.saldo = pontuacao_total
        salvar_progresso(jogador_atual)
        pontos_label.configure(text=f"PONTOS: {int(pontuacao_total)}")

    for alt in pergunta["respostas"]:
        letra = alt[0]
        btn = ctk.CTkButton(
            card, text=alt, width=680, height=60, 
            font=("Arial", 18, "bold"), fg_color="#334155", 
            command=lambda l=letra: responder(l)
        )
        btn.pack(pady=7)
        lista_botoes[letra] = btn

    # Rodapé
    rodape = ctk.CTkFrame(app, fg_color="transparent")
    rodape.pack(pady=25)
    
    ctk.CTkButton(
        rodape, text="PRÓXIMA PERGUNTA", width=280, height=55, 
        font=("Arial Black", 16), fg_color=COR_BOTAO_PADRAO, command=tela_jogo
    ).pack(side="left", padx=15)
    
    ctk.CTkButton(
        rodape, text="VOLTAR AO MENU", width=280, height=55, 
        font=("Arial Black", 16), fg_color="transparent", border_width=2, command=tela_menu
    ).pack(side="right", padx=15)

tela_menu()
app.mainloop()