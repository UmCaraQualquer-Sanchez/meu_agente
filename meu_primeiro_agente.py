from cerebro import Cerebro

meu_jarvis = Cerebro()
print("Jarvis online!!!(digite 'sair' para encerrar)\n")

while True:
    mensagem = input("Voce ")
    if mensagem.lower() == 'sair':
        print("desligando o sistema. ate logo, senhor.")
        break
    respota_do_cerebro = meu_jarvis.processar_mensagem(mensagem)
    print(f"Jarvis: {respota_do_cerebro}\n")