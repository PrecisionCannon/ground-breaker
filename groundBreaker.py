import discord, random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def rollDie(message, command: str):
    count: float
    sides: int

    try:
        [count, sides] = command.split("d", 2)
        count = float(count)
        if count % 1 == 0:
            count = int(count)
        sides = int(sides)
    except Exception as E:
        error: str = f"Failure rolling die {command} due to improper input. \nError: {E}"
        print(error)
        await message.channel.send(error)
        return None
    
    rolls = []
    for i in range(count):
        rolls.append(random.randint(1, sides))
        print(f"{rolls[i]}")
    total = sum(rolls)

    await message.channel.send(f"rolling {count} {sides}-sided dice. \nResults: {rolls} \nSum: {total}")

    return total

async def parseRollsCommand(message):
    command: str = message.content
    commandName: str
    commandInput: str
    [commandName, commandInput] = command.split(" ", 2)
    subcommands: list[str] = commandInput.split(r"\+")
    results: list[float] = []
    total: float
    for subcommand in subcommands:
        if subcommand.isnumeric():
            result = float(subcommand)
            if result % 1 == 0:
                result = int(result)
            results.append(result)
        if subcommand.find("d") != -1:
            result = await rollDie(message, subcommand)
            results.append(result)
    await message.channel.send(f"Final total: {results}")

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith(".roll"):
        result = await parseRollsCommand(message)
        #await message.channel.send(result)

client.run("MTE4NTQ4MjEwNTI0NTk0MTgyMg.GT60JS.bKQ6_NXFw0kSI40ues_hkWGL2SOBU76I3BeEOQ")