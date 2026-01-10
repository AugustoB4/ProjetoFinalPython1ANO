# ProjetoFinalPython1ANO
Esse é um projeto coordenado por Alessandro Rolim, para conclusão do 4º bimestre do curso de informática, primeiro ano.

Show do Milhão - Python Edition
Este é um jogo de perguntas e respostas inspirado no famoso programa de TV "Show do Milhão". O projeto conta com um sistema de cadastro de usuários, níveis de dificuldade e um ranking global.

🚀 Funcionalidades
Sistema de Usuários: Cadastro e Login com validação de senha (mínimo de 8 caracteres, contendo letras e números).

Dois Modos de Jogo:

Terminal: Versão clássica via linha de comando (main.py).

Interface Gráfica: Versão moderna utilizando a biblioteca customtkinter (interface.py).

Banco de Perguntas: Perguntas categorizadas por áreas (Matemática, História, Português, etc.) e níveis de dificuldade (fácil, médio, difícil).

Sistema de Pontuação e Ranking: As pontuações são salvas em um arquivo JSON e podem ser visualizadas em um ranking ordenado.

Persistência de Dados: Jogadores e perguntas são armazenados em arquivos .json dentro da pasta Data/.

📂 Estrutura do Projeto
main.py: Ponto de entrada para a versão via terminal.

interface.py: Interface gráfica completa utilizando CustomTkinter.

funcoes.py: Contém toda a lógica de negócio, manipulação de arquivos e validações.

classes.py: Define a classe jogador utilizada no sistema.

Data/:

jogadores.json: Armazena os dados de login e pontuação dos usuários.

perguntas.json: Banco de dados com as questões do jogo.

🛠️ Tecnologias Utilizadas
Python 3

CustomTkinter: Para a interface gráfica.

JSON: Para armazenamento de dados.

Pathlib/Time/Random: Bibliotecas padrão para gestão de caminhos, pausas dramáticas e sorteio de questões.

🔧 Como Executar
Instale as dependências (necessário para a versão com interface):

Bash

pip install customtkinter
Execute o jogo:

Para jogar no Terminal:

Bash

python main.py
Para jogar com Interface Gráfica:

Bash

python interface.py
📝 Regras do Jogo
No modo terminal, você escolhe entre responder perguntas e acumular pontos ou visualizar o ranking.

Na interface gráfica, cada resposta correta soma R$ 1.000,00 ao seu saldo, enquanto erros reduzem seu saldo pela metade.

Desenvolvido como um projeto educacional de lógica de programação em Python.