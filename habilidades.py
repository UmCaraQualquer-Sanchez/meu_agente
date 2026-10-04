import datetime

def obter_hora_atual():
    """Consulta o sistema e retorna a data e hora atual."""
    agora = datetime.datetime.now()
    return agora.strftime("Hoje é %d/%m/%Y e agora são %H:%M")