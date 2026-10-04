import datetime
import os
import webbrowser

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

def pesquisar_no_google(termo: str):
    """Abre o navegador padrão e faz uma pesquisa no Google sobre o termo."""
    try:   
        url = f"https://www.google.com/search?q={termo}"
        webbrowser.open(url)
        return f"pesquisa por '{termo}' aberta com sucesso no navegador"
    except Exception as erro:
        return f"Falha ao tentar abrir o navegador. Detalhe: {erro}"
