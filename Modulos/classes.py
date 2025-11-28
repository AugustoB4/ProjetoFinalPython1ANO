class jogador:
    def __init__(self, nome, dinheiro, rank, senha):
        self.nome = nome
        self.dinheiro = dinheiro
        self.rank = rank
        self.senha = senha
    
    def atualizar_dinheiro(self, valor):
        self.dinheiro += valor
    
    def atualizar_rank(self, novo_rank):
        self.rank = novo_rank