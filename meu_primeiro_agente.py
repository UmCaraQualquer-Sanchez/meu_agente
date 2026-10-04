import pyttsx3
from cerebro import Cerebro

motor_voz = pyttsx3.init()

motor_voz.setProperty('rate', 210)

def falar(texto):
    """Imprime na tela e fala o texto em voz alta simultaneamente."""
    print(f"Jarvis; {texto}\n")
    motor_voz.say(texto)
    motor_voz.runAndWait()

meu_jarvis = Cerebro()

falar("sistemas online.Estou pronto , senhor.")
print("(digite 'sair' para encerrar)\n")

while True:
    mensagem = input("Você: ")
    if mensagem.strip().lower() == 'sair':
        print("Desligando o sistema. ate logo, senhor.")
        break
    resposta_do_cerebro = meu_jarvis.processar_mensagem(mensagem)
    falar(resposta_do_cerebro)