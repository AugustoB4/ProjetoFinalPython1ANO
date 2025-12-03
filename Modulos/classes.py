class jogador:
    def __init__(self, nome, senha,):
        self.nome = nome
        self.senha = senha

    def pontuação(self, pontos, dinheiro, rank):
        self.pontos = pontos
        self.dinheiro = dinheiro
        self.rank = rank
        
    def atualizar_dinheiro(self, valor):
        self.dinheiro += valor
    
    def atualizar_rank(self, novo_rank):
        self.rank = novo_rank