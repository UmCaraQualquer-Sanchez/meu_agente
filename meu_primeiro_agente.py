import win32com.client
from cerebro import Cerebro
import os 
import wave 
import sounddevice as sd
import numpy as np 
 
motor_voz = win32com.client.Dispatch("SAPI.SpVoice")
motor_voz.Rate = 3

def falar(texto):
    texto_limpo = str(texto).strip()
    print(f"JARVIS: {texto_limpo}\n") 
    motor_voz.Speak(texto_limpo)

def ouvir_com_groq(cerebro_obj):
    #Grava o microfone localmente e usa o Whisper da Groq para transcrever
    taxa_amostragem = 16000
    duracao = 5
    arquivo_temp = "temp_audio.wav"

    print("[escutando...Fale agora]")
    #grava o adudio
    audio_sinal = sd.rec(int(duracao * taxa_amostragem), samplerate=taxa_amostragem, channels=1, dtype='int16')
    sd.wait()
    print("[Processando audio com whisper do groq...]")

    #salva temporariamente
    with wave.open(arquivo_temp, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) # 16-bit
        wf.setframerate(taxa_amostragem)
        wf.writeframes(audio_sinal.tobytes())
    try: 
        with open(arquivo_temp, "rb") as arquivo:
            transcricao = cerebro_obj.client.audio.transcriptions.create(
                file=(arquivo_temp, arquivo.read()),
                model="whisper-large-v3-turbo",
                language="pt",
                response_format="text"
            )
        texto = transcricao if isinstance(transcricao, str) else transcricao.text
        texto_limpo = texto.strip()

        if texto_limpo:
            print(f"Você: {texto_limpo}")
            return texto_limpo
        return ""
    except Exception as e:
        print(f"Erro na transcrição: {e}")
        return ""
    finally:
        if os.path.exists(arquivo_temp):
            os.remove(arquivo_temp)

    
meu_jarvis = Cerebro()

falar("Sistemas online. Estou pronto, senhor.")
print("(O microfone gravará automaticamente por 5 segundos a cada ciclo. Diga 'sair' para encerrar)\n")

while True:
    mensagem = ouvir_com_groq(meu_jarvis)
    
    if not mensagem:
        print("[ silêncio ou nada compreendido, ouvindo novamente... ]\n")
        continue
        
    if 'desligue todos os sistemas' in mensagem.lower():
        falar("Desligando o sistema. Até logo, senhor.")
        break
        
    resposta_do_cerebro = meu_jarvis.processar_mensagem(mensagem)
    
    falar(resposta_do_cerebro)