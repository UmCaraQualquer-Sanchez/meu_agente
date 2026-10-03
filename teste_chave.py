import os
from dotenv import load_dotenv

# Passo 1: O Python lê o arquivo .env e joga as informações na memória
load_dotenv()

# Passo 2: Tentamos resgatar o valor exato da chave pelo nome que demos a ela
minha_chave = os.getenv("GEMINI_API_KEY")

# Passo 3: Verificamos se deu certo
if minha_chave:
    print("Sucesso! O Python encontrou a chave escondida.")
    # Vamos imprimir só os 4 primeiros caracteres para confirmar, 
    # garantindo que a chave não vaze inteira na tela.
    print(f"Início da chave: {minha_chave[:4]}...")
else:
    print("Erro: A chave não foi encontrada. Verifique o arquivo .env.")