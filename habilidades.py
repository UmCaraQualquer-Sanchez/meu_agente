import datetime
import os

def obter_hora_atual():
    """Consulta o sistema e retorna a data e hora atual."""
    agora = datetime.datetime.now()
    return agora.strftime("Hoje é %d/%m/%Y e agora são %H:%M")

def abrir_spotify():
    """abre o spotify do usuario"""
    try:
        os.startfile("spotify:")
        return "Comando enviado para abrir o spotify enviado com sucesso."
    except Exception as erro:
        return f"Falha na tentativa de abrir o spotify. Detalhe: {erro}"