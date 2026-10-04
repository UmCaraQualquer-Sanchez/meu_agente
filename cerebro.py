import os
from dotenv import load_dotenv
from google import genai 
from google.genai import types
from habilidades import obter_hora_atual

class Cerebro:
    def __init__(self):
        print("iniciando módulos de inteligência...")
        load_dotenv()
        minha_chave = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=minha_chave)

        print("iciando o cérebro do Jarvis...")
        instrucao = (
             "Você é o JARVIS, assistente pessoal do Sanchez, um estudante "
            "de Ciência da Computação. Seja direto, técnico e prestativo. "
            "Nunca se apresente como um modelo do Google."
        )
        self.chat = self.client.chats.create(model='gemini-3.8-flash',
        config = types.GenerateContentConfig(system_instruction=instrucao,
        tools=[obter_hora_atual]),
        )

    def processar_mensagem(self, mensagem_do_usuario):
            try:
                resposta = self.chat.send_message(mensagem_do_usuario)
                return resposta.text

            except Exception as erro:
                return f"erro de comunicação: {erro}"
            

