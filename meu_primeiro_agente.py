import win32com.client
from cerebro import Cerebro

motor_voz = win32com.client.Dispatch("SAPI.SpVoice")
motor_voz.Rate = 3

def falar(texto):
    texto_limpo = str(texto).strip()
    print(f"JARVIS: {texto_limpo}\n") 
    motor_voz.Speak(texto_limpo)

meu_jarvis = Cerebro()

falar("Sistemas online. Estou pronto, senhor.")
print("(Digite 'sair' para encerrar)\n")

while True:
    mensagem = input("Você: ")
    if mensagem.strip().lower() == 'sair':
        falar("Desligando o sistema. Até logo, senhor.")
        break
    
    resposta_do_cerebro = meu_jarvis.processar_mensagem(mensagem)
    falar(resposta_do_cerebro)