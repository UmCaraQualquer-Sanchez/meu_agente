import os
import json
from dotenv import load_dotenv
from groq import Groq
from habilidades import obter_hora_atual, abrir_spotify, pesquisar_no_google

class Cerebro:
    def __init__(self):
        print("Iniciando módulos de inteligencia Groq (Llama 3)...")
        load_dotenv()
        minha_chave = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=minha_chave)

        print("Iniciando o cerebro do Jarvis...")
        instrucao = (
            "Você é o JARVIS, assistente pessoal do Sanchez, um estudante "
            "de Ciência da Computação. Seja direto, técnico e prestativo. "
            "IMPORTANTE: Suas respostas serão lidas por um sintetizador de voz. "
            "Gere textos limpos, como em um roteiro de fala humana. "
            "NUNCA use formatação Markdown, como asteriscos, negritos, listas ou símbolos especiais."
        )
        
        # memoria
        self.historico = [
            {"role": "system", "content": instrucao} 
        ]

        # Ferramentas
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "obter_hora_atual",
                    "description": "Consultar o sistema e retornar a data e a hora atual"
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "abrir_spotify",
                    "description": "Abre o aplicativo Spotify no computador do usuario"
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "pesquisar_no_google",
                    "description": "Abre o navegador e faz uma pesquisa no google",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "termo": {"type": "string", "description": "O termo a ser pesquisado"}
                        },
                        "required": ["termo"]
                    }
                }
            } 
        ]

    def processar_mensagem(self, mensagem_do_usuario):
        try:
            # salvar na memoria
            self.historico.append({"role": "user", "content": mensagem_do_usuario})

            resposta = self.client.chat.completions.create(
                model="qwen/qwen3.8-27b",
                messages=self.historico,
                tools=self.tools,
                tool_choice="auto" ,
                max_tokens = 950
            )

            mensagem_resposta = resposta.choices[0].message

            # logica das ferramentas
            if mensagem_resposta.tool_calls: 
                for tool_call in mensagem_resposta.tool_calls:
                    nome_function = tool_call.function.name

                    # evitar erro json de nao ter parametros
                    argumentos_str = tool_call.function.arguments
                    argumentos = json.loads(argumentos_str) if argumentos_str else {}

                    # roteador
                    if nome_function == "obter_hora_atual":
                        resultado = obter_hora_atual() 
                    elif nome_function == "abrir_spotify":
                        resultado = abrir_spotify() 
                    elif nome_function == "pesquisar_no_google":
                        resultado = pesquisar_no_google(argumentos.get("termo")) 
                    else:
                        resultado = "função nao encontrada" 
                        
                    # registra na memoria
                    self.historico.append(mensagem_resposta)
                    self.historico.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": nome_function,
                        "content": str(resultado)
                    }) 
                    
                resposta_final = self.client.chat.completions.create(
                    model="qwen/qwen3.8-27b",
                    messages=self.historico,
                    max_tokens = 950
                )
                
                texto_final = resposta_final.choices[0].message.content
                self.historico.append({"role": "assistant", "content": texto_final}) 
                return texto_final
                
            texto_resposta = mensagem_resposta.content
            self.historico.append({
                "role": "assistant", "content": texto_resposta 
            })
            return texto_resposta
            
        except Exception as erro:
            return f"erro na nova comunicação: {erro}"