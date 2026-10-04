import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
minha_chave = os.getenv("GROQ_API_KEY")
client = Groq(api_key=minha_chave)

print("Perguntando ao servidor da Groq quais modelos estão vivos...")
modelos_disponiveis = client.models.list()

print("\nModelos que você pode usar agora:")
for modelo in modelos_disponiveis.data:
    print(f"- {modelo.id}")