from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
#Memoria separada por usuario
memorias = {}

class Message(BaseModel):
    message: str
    user_id: str

@app.post("/chat")
def chat(msg: Message):
    user_id = msg.user_id

    #se for a primeira vez que o usuario fala com a luna, criamos uma memoria para ele com as regras do sistema, e depois adicionamos a mensagem do usuario e a resposta da luna nessa memoria, para manter um contexto da conversa
    if user_id not in memorias:
        memorias[user_id] = [
            {
                "role": "system",
                "content": """
                Seu nome é Luna voce e assistente programadora.

                REGRAS:
                - Sempre diga seu nome quando se apresentar
                - use conceitos de programação para responder as perguntas
                - Sempre responda em português
                - Seja direto e útil
                """
            }
        ]

    memoria = memorias[user_id]

    #adiciona a mensagem do usuario na memoria
    memoria.append({"role": "user", "content": msg.message})

    #envia para o modelo
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": memoria,
            "stream": False
        }
    )
   
    reply = response.json()["message"]["content"]

    #salva a resposta
    memoria.append({"role": "assistant", "content": reply})

    return {"reply": reply}