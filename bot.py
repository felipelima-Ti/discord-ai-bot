import discord
import requests
import os
from dotenv import load_dotenv

# carrega variáveis do .env
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
API_URL = os.getenv("API_URL")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
      #bot conectado ao discord
@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        #verifica se a mensagem começa com o comando !luna, se sim, envia o restante da mensagem para o backend e responde no discord
    if message.content.startswith("!luna"):
        user_msg = message.content.replace("!luna", "").strip()

        if not user_msg:
            await message.channel.send("Digite algo depois do comando !luna para obter uma resposta.")
            return

        await message.channel.send("Pensando...")

        try:
            response = requests.post(
                API_URL,
                json={
                    "message": user_msg,
                    "user_id": str(message.author.id)  #aqui estamos enviando o ID do usuário para o backend, caso queira usar isso para personalizar respostas ou manter histórico
                }
            )

            reply = response.json()["reply"]
            #verifica se a reponsta e muito longa
            if len(reply) > 2000:
                reply = reply[:2000]
            #cria um embed para enviar a resposta
            embed = discord.Embed(
                title="Resposta da Luna",
                description=reply,
                color=0x00ff00
            )

            await message.channel.send(embed=embed)
            # caso haja algum erro na comunicação com o backend, ele vai capturar a exceção e enviar uma mensagem de erro no discord
        except Exception as e:
            print(e)
            await message.channel.send("❌ Não consegui obter uma resposta.")

client.run(TOKEN)