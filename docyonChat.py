import openai

# Chave da API da OpenAI
chave_da_api = "COLOQUE SUA API_KEY AQUI"

openai.api_key = chave_da_api

# Criando variável para armazenamento do histórico de mensagens.
lista_de_mensagens = []

#--------------------MOCK--------------------
# Caso deseje testar usando o MOCK, mantenha "True", ou altere para "False" para usar a sua API real.
modo_teste = True

# Criando MOCK para que possamos testar o Chat.
def mock_chat_completion_create(model, messages):

    ultima_mensagem = messages[-1]["content"]
    resposta_fake = f"Você disse: '{ultima_mensagem}'. Isso é muito interessante! =)"

    return type("MockResponse", (), {
        "choices": [type("Choice", (), {
            "message": type("Message", (), {"content": resposta_fake})
        })()]
    })()

# Substitui a chamada real pela mockada
if modo_teste:
    openai.chat.completions.create = mock_chat_completion_create
#--------------------------------------------

# Declarando função para enviar mensagem para o modelo do ChatGPT.
def enviar_conversa(mensagem, lista_de_mensagens=[]):

    lista_de_mensagens.append(
        {"role":"user", "content":mensagem}
    )

    resposta = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = lista_de_mensagens,
    )
    return resposta.choices[0].message.content

# Solicita uma mensagem ao usuário. 
# Caso escreva "sair", o chat é encerrado. 
# Adiciona a resposta do modelo ao histórico.
while True:
    texto = input("O que esta pensando?")

    if texto == "sair":
        break
    else:
        resposta = enviar_conversa(texto, lista_de_mensagens)
        lista_de_mensagens.append({'role':'assistant','content':resposta})
        print("Docyon:", resposta)