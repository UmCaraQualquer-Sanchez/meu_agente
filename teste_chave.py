import os
from dotenv import load_dotenv

load_dotenv()

minha_chave = os.getenv("GEMINI_API_KEY")

if minha_chave:
    print("Sucesso! O Python encontrou a chave escondida.")
    print(f"Início da chave: {minha_chave[:4]}...")
else:
    print("Erro: A chave não foi encontrada. Verifique o arquivo .env.")