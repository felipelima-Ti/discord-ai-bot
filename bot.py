import discord
import requests
# Substitua pelo token do seu bot do Discord
TOKEN = ""

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# URL de configuração do seu agente de IA, certifique-se de que o agente esteja rodando e acessível nesse endereço
API_URL = ""

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")# inicialização do bot, imprime no console quando estiver pronto

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # prefixo configurado para receber o comando !ai
    if message.content.startswith("!ai"):
        user_msg = message.content.replace("!ai", "").strip()

        if not user_msg:
            await message.channel.send("Digite algo depois do coando !ai para obter uma resposta.")
            return

        await message.channel.send("aguarde um pouco, estou Pensando...")
        #tenta obter uma resposta do agente, se der erro, avisa o usuário
        try:
            response = requests.post(
                API_URL,
                json={"message": user_msg}
            )

            reply = response.json()["reply"]

            # evita mensagens muito grandes que podem causar problemas
            if len(reply) > 2000:
                reply = reply[:2000]
            #cria um embed para enviar a resposta
            embed = discord.Embed(
                title="Resposta da IA",
                description=reply,
                color=0x00ff00
            )

            await message.channel.send(embed=embed)

        except Exception as e:
            await message.channel.send("Não consegui obter uma resposta 😥")

client.run(TOKEN)