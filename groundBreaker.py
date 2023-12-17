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
    if message.content.startswith(".sayhi"):
        await message.channel.send("Hi everyone, Vi- made me")
    if message.content.startswith(".help opensource"):
        githublink = "https://github.com/PrecisionCannon/ground-breaker"
        await message.channel.send(f"I'm open source. You can download me at {githublink} and run me if you have your own bot registered with Discord. \nYou're also welcome to add my features to your own bots")
    if message.content.startswith(".help dice"):
        await message.channel.send("I can roll dice and do arithmetic. \nType in `.roll` and then any combination of numbers, arithmetic operators, and dice rolls. \nI can't do brackets yet though")
    if message.content.startswith(".help music"):
        await message.channel.send("Vi- is working on some code that will let me play music from Youtube in voice channels")
    if message.content.startswith(".roll"):
        await groundBreakerDice.parseRollsCommand(message)
    if message.content.startswith(".connect"):
        await groundBreakerVoice.parseConnectCommand(message)
        

tokenFile = open("token.txt")
token: str = tokenFile.read()
client.run(token)