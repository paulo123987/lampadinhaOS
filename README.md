# lampadinhaOS
DADOS: AS LIÇÕES DO LAMPADINHA (Soft Skills)
## 🚀 Como Executar

```bash
# 1. Criar e ativar ambiente
conda create --name lampadinha python=3.11
conda activate lampadinha

# 2. Instalar pip e dependências
conda install pip
pip install -r requirements.txt

# 5. Iniciar o app
python app.py
```

🚀 Lampadinha OS – Innovation Hub

Lampadinha OS é uma aplicação interativa construída com Python + Gradio + IA (Groq + Llama 3) que simula o assistente robótico Lampadinha, ajudante do Professor Pardal.

O objetivo do sistema é criar um hub de inovação, cultura organizacional e brainstorming corporativo, combinando:

🤖 Inteligência Artificial

🧠 Soft Skills

💡 Cultura organizacional

🐍 Geração de código em Python

🎨 Interface interativa com Gradio

A aplicação foi projetada para rodar facilmente em ambientes como:

Hugging Face Spaces

Servidores Python

Ambientes locais de desenvolvimento

🧠 Conceito do Projeto

O projeto usa o personagem Lampadinha, o robô inventor do Professor Pardal, como metáfora para um assistente criativo de inovação.

Ele atua em três frentes principais:

1️⃣ Consultoria de projetos com IA
2️⃣ Reflexões de cultura organizacional
3️⃣ Geração de scripts Python inspiradores

🏗 Arquitetura da Aplicação
Lampadinha OS
│
├── app.py / app_haggingface.py
│
├── Funções principais
│   ├── consultar_lampadinha()
│   ├── gerar_codigo_lampadinha()
│   └── gerar_card_licao()
│
├── Banco de dados interno
│   └── licoes_db (soft skills)
│
└── Interface
    └── Gradio Blocks
🧩 Tecnologias Utilizadas
Tecnologia	Função
Python	Linguagem principal
Gradio	Interface web interativa
Groq API	Integração com IA
Llama 3.1	Modelo de linguagem
Markdown / HTML	Renderização de conteúdo
🔑 Configuração da API

A aplicação usa a API do Groq para acessar o modelo Llama 3.1.

A chave não fica no código, sendo carregada via variável de ambiente:

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

Isso permite rodar o projeto com segurança em ambientes como:

Hugging Face Spaces

Docker

servidores cloud

Configurar variável de ambiente

Linux / Mac:

export GROQ_API_KEY="sua_chave_aqui"

Windows:

setx GROQ_API_KEY "sua_chave_aqui"
🧠 Banco de Dados de Lições

O sistema possui um pequeno banco interno chamado:

licoes_db

Ele contém lições inspiradas no comportamento do Lampadinha, como:

🤲 Servir com humildade

🧠 Inteligência com simplicidade

🤝 Lealdade

🎨 Criatividade

😊 Alegria em ajudar

🌱 Pequenas atitudes fazem diferença

Essas lições são usadas para gerar cards visuais na interface.

⚙️ Funcionalidades
💬 1. Consultoria em Projetos (IA)

Permite que o usuário descreva um problema organizacional.

Exemplo:

Como melhorar a comunicação interna da equipe?

A IA responde como o Lampadinha, usando analogias com invenções e criatividade.

Função responsável:

consultar_lampadinha()
✨ 2. Cultura & Valores

Mostra reflexões sobre cultura organizacional usando o banco interno de lições.

Cada reflexão é exibida como um card visual estilizado.

Função responsável:

gerar_card_licao()

O usuário pode:

selecionar um valor

gerar uma reflexão aleatória

🐍 3. Código do Lampadinha

Uma funcionalidade criativa onde o usuário digita um tema, e a IA gera um script Python inspirado nesse tema.

Exemplo:

Trabalho em equipe

Saída:

# Script Python inspirado em colaboração

def trabalhar_em_equipe():
    membros = ["ideia", "cooperação", "respeito"]

    for valor in membros:
        print(f"Construindo sucesso com {valor}")

trabalhar_em_equipe()

Função responsável:

gerar_codigo_lampadinha()
🎨 Interface

A interface foi construída com Gradio Blocks e possui:

📌 Cabeçalho

Lampadinha

Branding visual

📑 Três abas principais
💬 Consultoria em Projetos
✨ Cultura & Valores
🐍 Código do Lampadinha

A interface também inclui elementos visuais como:

Professor Pardal

Tio Patinhas

Cards de cultura

🚀 Como Executar Localmente
1️⃣ Criar ambiente
conda create --name lampadinha python=3.11
conda activate lampadinha
2️⃣ Instalar dependências
pip install gradio
pip install groq

ou usando requirements:

pip install -r requirements.txt
3️⃣ Executar a aplicação
python app.py

ou

python app_haggingface.py
🌐 Executar no Hugging Face Spaces

Criar um Space

Escolher SDK: Gradio

Fazer upload dos arquivos

Adicionar o secret:

GROQ_API_KEY


👨‍💻 Autor

Projeto desenvolvido para estudo de:

IA aplicada

Cultura organizacional

Interfaces interativas com Python

📜 Licença

MIT License

💡 Lampadinha diz:
"Toda grande invenção começa com uma pequena faísca de curiosidade."

