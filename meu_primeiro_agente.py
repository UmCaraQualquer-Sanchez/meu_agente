import os
from dotenv import load_dotenv
from google import genai

# 1. Configuração inicial (igual ao que já tínhamos)
load_dotenv()
minha_chave = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=minha_chave)

print("Iniciando o cérebro do JARVIS...")
chat = client.chats.create(model='gemini-3.8-flash')
print("JARVIS online! (Digite 'sair' para encerrar)\n")

# 2. O Loop principal do programa (igual ao while em C)
while True:
    # input() é o scanf do Python. Ele pausa e espera o usuário digitar.
    mensagem = input("Você: ")
    
    # Condição de saída (break funciona igualzinho em C)
    if mensagem.lower() == 'sair':
        print("Desligando o sistema. Até logo, senhor.")
        break
        
    # 3. Bloco de Proteção
    # O "try" diz para o Python: "Tente fazer isso. Se der erro, não feche o programa, pule para o except".
    try:
        resposta = chat.send_message(mensagem)
        print(f"JARVIS: {resposta.text}\n")
    
    except Exception as erro:
        # Se o servidor der erro 503 de novo, ele cai aqui, avisa, e o loop recomeça!
        print(f"JARVIS: Desculpe, tive um problema de comunicação com o servidor.\n(Detalhe técnico: {erro})\n")