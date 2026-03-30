from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Prompts e memória do seu agente 
memoria = [
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

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(msg: Message):
    memoria.append({"role": "user", "content": msg.message})
# Envie a conversa para o modelo de ia para uma resposta 
    response = requests.post(
        # url padrao do agent, se tiver outro modelo ou porta, mude aqui
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",
            "messages": memoria,
            "stream": False
        }
    )
    #resposta do modelo para o bot, que sera enviada para o discord
    reply = response.json()["message"]["content"]

    memoria.append({"role": "assistant", "content": reply})

    return {"reply": reply}