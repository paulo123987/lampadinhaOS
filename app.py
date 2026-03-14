import gradio as gr
import random
import os

# Tenta importar o Groq. Se o usuário não tiver, avisaremos no console.
try:
    from groq import Groq
except ImportError:
    print("⚠️ Biblioteca 'groq' não encontrada. Instale com: pip install groq")

# ---------------------------------------------------------
# CONFIGURAÇÃO DA API DO GROQ (Produção Segura)
# ---------------------------------------------------------
# Em vez de deixar a chave exposta no código, pegamos ela do cofre de Secrets do Hugging Face.
GROQ_API_KEY = os.environ.get("GROQ_API_KEY") 

def obter_cliente_groq():
    if not GROQ_API_KEY:
        return None
    return Groq(api_key=GROQ_API_KEY)

# ---------------------------------------------------------
# DADOS: AS LIÇÕES DO LAMPADINHA (Soft Skills)
# ---------------------------------------------------------
licoes_db = [
    {
        "icone": "🤲", 
        "tema": "Servir com humildade", 
        "contexto": "Lampadinha sempre ajuda o Professor Pardal sem buscar reconhecimento.", 
        "licao": "Grandes pessoas não precisam de aplausos para fazer o bem. A verdadeira grandeza está em servir."
    },
    {
        "icone": "🧠", 
        "tema": "Inteligência com simplicidade", 
        "contexto": "Mesmo sendo pequeno, Lampadinha muitas vezes resolve problemas que ninguém consegue.", 
        "licao": "Não subestime quem parece simples. Sabedoria não depende de tamanho, posição ou aparência."
    },
    {
        "icone": "🤝", 
        "tema": "Lealdade", 
        "contexto": "Lampadinha é extremamente fiel ao Professor Pardal, mesmo quando as invenções dão errado.", 
        "licao": "A lealdade é uma das maiores virtudes nos relacionamentos."
    },
    {
        "icone": "🎨", 
        "tema": "Criatividade para resolver problemas", 
        "contexto": "Ele sempre encontra soluções criativas para situações difíceis.", 
        "licao": "Problemas não são o fim — são oportunidades para usar a criatividade."
    },
    {
        "icone": "😊", 
        "tema": "Alegria em ajudar", 
        "contexto": "Lampadinha demonstra satisfação em ajudar os outros.", 
        "licao": "A felicidade verdadeira muitas vezes está em contribuir para o sucesso de alguém."
    },
    {
        "icone": "🌱", 
        "tema": "Pequenas atitudes, grande diferença", 
        "contexto": "Embora seja pequeno, Lampadinha muitas vezes salva o dia.", 
        "licao": "Não existe gesto pequeno quando ele é feito com amor e dedicação."
    }
]

# ---------------------------------------------------------
# FUNÇÕES DE LÓGICA
# ---------------------------------------------------------

def consultar_lampadinha(pergunta):
    """Função que usa a IA do Groq para brainstorming"""
    client = obter_cliente_groq()
    if not client:
        return "⚠️ Erro: A API Key do Groq não foi encontrada nos 'Secrets' do Hugging Face!"
    
    if not pergunta.strip():
        return "⚠️ Bzzzt! Meus sensores não detectaram nenhuma pergunta."

    system_prompt = """Você é o Lampadinha, o assistente robô do Professor Pardal.
    Você ajuda profissionais a resolver problemas e inovar.
    Responda em português do Brasil. Seja otimista, genial e use analogias com invenções.
    Seja prático e direto!"""

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Ajude-me com isso: {pergunta}"}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=500,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"🔌 Curto-circuito ao conectar com a IA: {str(e)}"

def gerar_codigo_lampadinha(tema):
    """Função que usa a IA do Groq para gerar lições em formato de código Python"""
    client = obter_cliente_groq()
    if not client:
        return "⚠️ Erro: A API Key do Groq não foi encontrada nos 'Secrets' do Hugging Face!"
    
    if not tema.strip():
        return "⚠️ Bzzzt! Digite um tema para eu compilar as minhas ideias."

    system_prompt = """Você é o Lampadinha, o assistente robô do Professor Pardal, mas agora você se comunica exclusivamente através de scripts em Python.
    O usuário fornecerá um tema. Você deve criar um pequeno script em Python válido, bem formatado e comentado.
    O código deve conter variáveis, funções ou classes que resolvam um problema fictício ou imprimam uma mensagem inspiradora sobre o tema.
    Use os comentários do código para dar conselhos sábios.
    SEMPRE retorne a resposta APENAS em um bloco markdown de código python (```python ... ```)."""

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Escreva um script Python inspirador sobre o tema: {tema}"}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=600,
        )
        resposta = chat_completion.choices[0].message.content
        return resposta
    except Exception as e:
        return f"🔌 Curto-circuito de Sintaxe: {str(e)}"

def gerar_card_licao(indice=None):
    """Gera um card HTML bonito com a lição selecionada ou uma aleatória"""
    if indice is None or indice == "Sorteio Aleatório 🎲":
        item = random.choice(licoes_db)
    else:
        # Encontra a lição pelo tema escolhido no dropdown
        item = next((l for l in licoes_db if l["tema"] == indice), licoes_db[0])
        
    # Aplicando a nova paleta de cores:
    # Color 1: rgb(207, 14, 14) (Borda e Título)
    # Color 2: rgb(219, 74, 74) (Linha separadora)
    # Color 4: rgb(243, 195, 195) (Fundo gradiente suave)
    # Color 5: rgb(255, 255, 255) (Fundo branco base)
    html = f"""
    <div style="background: linear-gradient(135deg, rgb(255, 255, 255) 0%, rgb(243, 195, 195) 100%); border-left: 6px solid rgb(207, 14, 14); border-radius: 12px; padding: 25px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin: 10px 0;">
        <div style="font-size: 2.5em; margin-bottom: 10px;">{item['icone']}</div>
        <h3 style="color: rgb(207, 14, 14); margin-top: 0; font-size: 1.4em;">{item['tema']}</h3>
        <p style="color: #475569; font-style: italic; font-size: 1.1em; margin-bottom: 15px;">"{item['contexto']}"</p>
        <hr style="border-top: 1px dashed rgb(219, 74, 74); margin: 15px 0;">
        <p style="color: #1e293b; font-weight: bold; font-size: 1.2em; line-height: 1.5;">💡 Lição: {item['licao']}</p>
    </div>
    """
    return html

# ---------------------------------------------------------
# INTERFACE GRADIO (FRONT-END CORPORATIVO)
# ---------------------------------------------------------

# Trocamos primary_hue para 'red' para combinar melhor com a nova paleta
tema_lampadinha = gr.themes.Soft(primary_hue="red", neutral_hue="slate")

with gr.Blocks(title="Lampadinha OS - Innovation Hub") as app:
    
    # CABEÇALHO
    with gr.Row():
        with gr.Column(scale=1, min_width=150):
            # Alterada a cor da borda e sombra da imagem para rgb(207, 14, 14)
            gr.HTML(
                """
                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                <img width="144" height="144" src="https://img.icons8.com/color/144/pixar-lamp.png" alt="pixar-lamp"/>
                </div>
                """
            )
        with gr.Column(scale=4):
            # Alterada a cor do título para rgb(207, 14, 14)
            gr.HTML("<h1 style='color: rgb(207, 14, 14); margin-bottom: 0;'>⚙️ Lampadinha OS</h1>")
            gr.Markdown("**Hub de Inovação, Cultura e Brainstorming Corporativo.**")
    
    gr.Markdown("---")
    
    with gr.Tabs():
        
        # ABA 1: CONSULTORIA DE PROJETOS (Mantemos a IA aqui!)
        with gr.Tab("💬 Consultoria em Projetos (IA)"):
            gr.Markdown("### Descreva o problema da sua equipe. A IA do Lampadinha vai analisar e propor soluções!")
            
            with gr.Row():
                with gr.Column(scale=1):
                    # Novo: Imagem e Quote do Professor Pardal
                    gr.HTML(
                        """
                        <div style="text-align: center; padding: 15px; margin-bottom: 15px; background: linear-gradient(135deg, rgb(255, 255, 255) 0%, rgb(243, 195, 195) 100%); border-radius: 12px; border: 2px dashed rgb(207, 14, 14);">
                            <img src="https://upload.wikimedia.org/wikipedia/en/5/52/Gyro_Gearloose.png" style="max-width: 90px; margin: 0 auto; border-radius: 8px;">
                            <p style="color: rgb(207, 14, 14); font-weight: bold; margin-top: 10px; font-size: 1.1em;">Prof. Pardal</p>
                            <p style="color: #475569; font-size: 0.9em; font-style: italic;">"Toda grande ideia começa com uma pequena engrenagem! O que vamos inventar hoje?"</p>
                        </div>
                        """
                    )
                with gr.Column(scale=2):
                    input_problema = gr.Textbox(
                        label="Situação / Desafio Atual",
                        placeholder="Ex: Como podemos melhorar a comunicação interna?",
                        lines=4
                    )
                    btn_consultar = gr.Button("🧠 Iniciar Brainstorming", variant="primary")
                    
                    gr.Examples(
                        examples=[
                            "Como podemos reduzir o tempo de onboarding de novos funcionários na equipe?",
                            "Qual a melhor forma de organizar o fluxo de aprovação de contratos?",
                            "Temos um orçamento pequeno. Como fazer uma campanha de valorização impactante?"
                        ],
                        inputs=input_problema,
                        label="💡 Exemplos de Desafios:"
                    )
                
                with gr.Column(scale=2):
                    output_consultoria = gr.Markdown(
                        label="Análise do Lampadinha",
                        value="*Aguardando entrada de dados nas engrenagens...*"
                    )
            
            btn_consultar.click(fn=consultar_lampadinha, inputs=[input_problema], outputs=output_consultoria)

        # ABA 2: CULTURA E VALORES
        with gr.Tab("✨ Cultura & Valores"):
            gr.Markdown("### As Lições do Lampadinha para o Dia a Dia")
            gr.Markdown("Apesar de ser pequeno e quase não falar, ele transmite lições cruciais para qualquer equipe de sucesso.")
            
            with gr.Row():
                with gr.Column(scale=1):
                    # Dropdown com os temas + opção aleatória
                    opcoes = ["Sorteio Aleatório 🎲"] + [l["tema"] for l in licoes_db]
                    seletor_licao = gr.Dropdown(choices=opcoes, value="Sorteio Aleatório 🎲", label="Escolha um pilar cultural:")
                    btn_licao = gr.Button("Gerar Reflexão 💡", variant="primary")
                    
                    # Novo: Imagem e Quote do Tio Patinhas
                    gr.HTML(
                        """
                        <div style="text-align: center; padding: 15px; margin-top: 20px; background: linear-gradient(135deg, rgb(255, 255, 255) 0%, rgb(243, 195, 195) 100%); border-radius: 12px; border: 2px dashed rgb(207, 14, 14);">
                            <img src="https://upload.wikimedia.org/wikipedia/en/1/13/Macduck.png" style="max-width: 80px; margin: 0 auto; border-radius: 8px;">
                            <p style="color: rgb(207, 14, 14); font-weight: bold; margin-top: 10px; font-size: 1.1em;">Tio Patinhas</p>
                            <p style="color: #475569; font-size: 0.9em; font-style: italic;">"Uma equipe com bons valores vale mais que todo o ouro da minha caixa-forte!"</p>
                        </div>
                        """
                    )

                with gr.Column(scale=2):
                    # Onde o card bonito vai aparecer
                    output_card = gr.HTML(value=gerar_card_licao("Sorteio Aleatório 🎲"))
                    
                    # A reflexão espiritual / aplicação no final
                    gr.HTML("""
                    <div style="margin-top: 20px; text-align: center; padding: 15px; border-top: 1px solid rgb(243, 195, 195);">
                        <p style="color: rgb(207, 14, 14); font-size: 1em; margin-bottom: 5px;">✅ <b>Aplicação Espiritual:</b></p>
                        <p style="color: #334155; font-style: italic;">
                            "Assim como Lampadinha ajuda o inventor, nós também fomos chamados para ser luz e ajudar os outros.<br>
                            Vós sois a luz do mundo. (Mateus 5:14)"
                        </p>
                    </div>
                    """)

            btn_licao.click(fn=gerar_card_licao, inputs=[seletor_licao], outputs=[output_card])

        # ABA 3: PYTHON DO LAMPADINHA (NOVA ABA)
        with gr.Tab("🐍 Código do Lampadinha"):
            gr.Markdown("### Transforme ideias em algoritmos!")
            gr.Markdown("Digite um tema e o Lampadinha escreverá um script inspirador em Python com comentários e lógicas sobre o assunto.")
            
            with gr.Row():
                with gr.Column(scale=1):
                    input_tema_codigo = gr.Textbox(
                        label="Tema para o Código",
                        placeholder="Ex: Trabalho em Equipe, Resolução de Conflitos, Superação...",
                        lines=2
                    )
                    btn_codigo = gr.Button("💻 Compilar Sabedoria", variant="primary")
                    
                    gr.Examples(
                        examples=[
                            "Resiliência e superação de falhas",
                            "Trabalho em equipe e colaboração",
                            "Encontrando soluções criativas"
                        ],
                        inputs=input_tema_codigo,
                        label="💡 Exemplos de Temas:"
                    )
                
                with gr.Column(scale=2):
                    output_codigo = gr.Markdown(
                        label="Terminal do Lampadinha",
                        value="*Aguardando compilação...*"
                    )
            
            btn_codigo.click(fn=gerar_codigo_lampadinha, inputs=[input_tema_codigo], outputs=output_codigo)

    gr.Markdown("---")
    gr.Markdown("<p style='text-align: center; color: gray; font-size: 0.8em;'>Tecnologia aliada à Cultura Organizacional.</p>")

if __name__ == "__main__":
    app.launch(theme=tema_lampadinha)
