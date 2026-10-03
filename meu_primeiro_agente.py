import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
minha_chave = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=minha_chave)

print("Iniciando o cérebro do JARVIS...")
chat = client.chats.create(model='gemini-3.8-flash')
print("JARVIS online! (Digite 'sair' para encerrar)\n")

while True:
    mensagem = input("Você: ")
    
    if mensagem.lower() == 'sair':
        print("Desligando o sistema. Até logo, senhor.")
        break
    
    try:
        resposta = chat.send_message(mensagem)
        print(f"JARVIS: {resposta.text}\n")
    
    except Exception as erro:
        print(f"JARVIS: Desculpe, tive um problema de comunicação com o servidor.\n(Detalhe técnico: {erro})\n")