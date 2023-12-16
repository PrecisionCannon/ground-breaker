import discord, random, re

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
    total = sum(rolls)

    await message.channel.send(f"rolling {count} {sides}-sided dice. \nResults: {rolls} \nSum: {total}")

    return total

async def parseRollsCommand(message):
    command: str = message.content
    commandName: str
    commandInput: str
    try:
        [commandName, commandInput] = command.split(" ", 2)
    except ValueError:
        error: str = f"Too many command strings. \nThere should only be a space after .roll, no other spaces"
        print(error)
        await message.channel.send(error)
    subcommands: list[str] = re.split(r"\+|-|\*|\/|\%|\^", commandInput)
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
    possibleOperators: str = "+-*/%^"
    operators: list[str] = []
    subcommandsIndex: int = 0
    total: float = results[subcommandsIndex]
    for character in commandInput:
        if possibleOperators.find(character) != -1:
            operators.append(character)
            subcommandsIndex = subcommandsIndex + 1
            if character == "+":
                total = total + results[subcommandsIndex]
            if character == "-":
                total = total - results[subcommandsIndex]
            if character == "*":
                total = total * results[subcommandsIndex]
            if character == "/":
                total = total / results[subcommandsIndex]
            if character == "%":
                total = total % results[subcommandsIndex]
            if character == "^":
                total = total ^ results[subcommandsIndex]
    
    await message.channel.send(f"Final total: {total}")

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

tokenFile = open("token.txt")
token: str = tokenFile.read()
client.run(token)