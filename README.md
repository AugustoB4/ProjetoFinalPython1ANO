# ProjetoFinalPython1ANO
Esse é um projeto coordenado por Alessandro Rolim, para conclusão do 4º bimestre do curso de informática, primeiro ano.

🎮 Perguntas e Respostas
📚 Tema do Projeto

O projeto Perguntas e Respostas é um jogo em Python no estilo quiz interativo, onde os jogadores podem se cadastrar, fazer login, responder perguntas de múltipla escolha, acumular pontos e competir em um ranking geral.
O objetivo é responder corretamente o maior número de perguntas possível para alcançar as melhores posições no ranking.

▶️ Instruções de Execução
Pré-requisitos:
Python 3.8 ou superior instalado
Terminal/Prompt de comando

Passo a passo:
Clone ou extraia o projeto para uma pasta:
git clone <repositorio>
ou simplesmente extraia os arquivos.

Certifique-se de que os seguintes arquivos estejam organizados dessa forma:
Módulos/
│
├── main.py
├── funcoes.py 
└── classes.py
Data/
│
├──perguntas.json
└── jogadores.json


Execute o jogo com:
python main.py


No menu inicial, você poderá:
1 - Cadastrar um novo jogador
2 - Entrar com um jogador existente
3 - Jogar a competição
4 - Visualizar o ranking
5 - Sair do jogo

📦 Bibliotecas Utilizadas
Bibliotecas padrão do Python:
json → leitura e escrita dos arquivos de perguntas e jogadores
time → uso de delays (sleep)
random → sorteio de perguntas
(Não há bibliotecas externas, apenas bibliotecas nativas do Python)

⚙️ Funcionalidades

✔ Sistema de cadastro de jogadores
✔ Sistema de login
✔ Sistema de pontuação
✔ Perguntas de múltipla escolha
✔ Sorteio aleatório de perguntas
✔ Ranking automático dos jogadores
✔ Armazenamento de dados em arquivos JSON
✔ Interface em terminal (CLI)
✔ Sistema de menu interativo
✔ Persistência de dados (pontuação salva)

🗂 Estrutura do Projeto
📁 projeto/
Módulos/
│
├── main.py (Arquivo principal, a qual apresenta toda a estrutura para rodar o jogo.)
├── funcoes.py (Onde se encontra todas as funções que estão dentro do jogo, incluindo o próprio.)
└── classes.py (Arquivo com o objeto jogador, que facilita o cadastro e salvamento de progresso dos usuários.)
Data/
│
├──perguntas.json (Todas as perguntas que irão aparecer na competição estão aqui.)
└── jogadores.json (Todos os jogadores e seus progressos são salvos nesse arquivo.)
README.md (Documentação do jogo.)

👥 Integrantes do Grupo
1 - Cezar Augusto
2 - Anthony Gabryel
3 - Gustavo Medeiros


🧠 Objetivo Educacional
Este projeto foi desenvolvido com fins educacionais, com foco em:
Programação em Python
Estruturas de dados
Funções
Classes e objetos (POO)
Manipulação de arquivos JSON
Lógica de programação
Organização de projeto
Estrutura modular de código