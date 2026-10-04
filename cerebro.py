import os
from dotenv import load_dotenv
from google import genai 

class Cerebro:
    def __init__(self):
        print("iniciando módulos de inteligência...")
        load_dotenv()
        minha_chave = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=minha_chave)

        print("iciando o cérebro do Jarvis...")
        self.chat = self.client.chats.create(model='gemini-3.8-flash')
        
    def processar_mensagem(self, mensagem_do_usuario):
            try:
                resposta = self.chat.send_message(mensagem_do_usuario)
                return resposta.text

            except Exception as erro:
                return f"erro de comunicação: {erro}"
            

