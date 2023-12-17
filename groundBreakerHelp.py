import discord

async def helpOpenSource(message):
    githublink = "https://github.com/PrecisionCannon/ground-breaker"
    await message.channel.send(f"I'm open source. You can download me at {githublink} and run me if you have your own bot registered with Discord. \nYou're also welcome to add my features to your own bots")
    
async def helpDice(message):
    await message.channel.send("""I can roll dice and do arithmetic. 
Type in `.roll` and then any combination of numbers and dice rolls separated by arithmetic operators, like `.roll 2d6+1`.
Supported operators: +, -, *, /, %, ^
I can't do brackets yet""")
    
async def helpMusic(message):
    await message.channel.send("Vi- is working on some code that will let me play music from Youtube in voice channels")
    

async def parseHelpCommand(message):
    if message.content.startswith(".help opensource"):
        await helpOpenSource(message)
        return
    if message.content.startswith(".help dice"):
        await helpDice(message)
        return
    if message.content.startswith(".help music"):
        await helpMusic(message)
        return

    await message.channel.send("""I'm a roleplaying assistant designed for Vi-'s campaign Ground Break. Available help subcommands:
`.help opensource`
`.help dice`
`.help music`
""")