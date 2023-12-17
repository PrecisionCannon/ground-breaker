import discord

import groundBreakerDice, groundBreakerVoice, groundBreakerHelp

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
voiceClient: discord.voice_client = None

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(".sayhi"):
        await message.channel.send("Hi everyone, Vi- made me")
    if message.content.startswith(".help"):
        await groundBreakerHelp.parseHelpCommand(message)
    if message.content.startswith(".roll"):
        await groundBreakerDice.parseRollsCommand(message)
    if message.content.startswith(".connect"):
        voiceClient = await groundBreakerVoice.parseConnectCommand(message)
    if message.content.startswith(".play"):
        await groundBreakerVoice.parsePlayCommand(message, voiceClient)
        
        

tokenFile = open("token.txt")
token: str = tokenFile.read()
client.run(token)