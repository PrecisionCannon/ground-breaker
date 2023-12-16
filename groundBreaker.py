import discord

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
    if message.content.startswith(".test"):
        await message.channel.send("Test successful")

client.run("MTE4NTQ4MjEwNTI0NTk0MTgyMg.GT60JS.bKQ6_NXFw0kSI40ues_hkWGL2SOBU76I3BeEOQ")