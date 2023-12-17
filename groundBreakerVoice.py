import youtube_dl
from discord import message, member, voice_client

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',  # bind to ipv4 since ipv6 addresses cause issues sometimes
}

async def connectToUser(message: message, member: member):
    voiceStatus = member.voice
    if voiceStatus == None:
        await message.channel.send("Error: You are not connected to a voice channel")
        return
    try:
        voiceClient = await voiceStatus.channel.connect()
        await message.channel.send(f"Connected to `{voiceStatus.channel}`")
    except Exception as E:
        await message.channel.send(f"Problem connecting: {E}")
    print(voiceClient)
    return voiceClient

async def parseConnectCommand(message: message):
    await connectToUser(message, message.author)
    
async def parsePlayCommand(message: message, voiceClient: voice_client = None):
    if voiceClient == None:
        voiceClient = await connectToUser(message, message.author)
    