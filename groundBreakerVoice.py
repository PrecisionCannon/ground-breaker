import discord
from discord import message, member

async def connectToUser(message: message, member: member):
    voiceStatus = member.voice
    if voiceStatus == None:
        await message.channel.send("Error: You are not connected to a voice channel")
        return
    try:
        voiceClient = await voiceStatus.channel.connect()
        await message.channel.send(f"Connected to {voiceStatus.channel}")
    except:
        await message.channel.send("Problem connecting")

async def parseConnectCommand(message: message):
    await connectToUser(message, message.author)
    