import discord

import groundBreakerDice, groundBreakerVoice

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(".roll"):
        await groundBreakerDice.parseRollsCommand(message)
    if message.content.startswith(".connect"):
        await groundBreakerVoice.parseConnectCommand(message)
        

tokenFile = open("token.txt")
token: str = tokenFile.read()
client.run(token)