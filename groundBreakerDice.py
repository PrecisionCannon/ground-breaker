import random, re
from operator import add, sub, mul, truediv, mod, pow

async def rollDie(message, command: str):
    count: float
    sides: int

    try:
        [count, sides] = command.split("d", 2)
        if count == "":
            count = 1
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

async def applyOperator(message, results: list[float], operators: list[str], operator):
    operatorKeys = {"+": add, "-": sub, "*": mul, "/": truediv, "%": mod, "^": pow}
    i = 0
    while i < len(operators):
        if operatorKeys[operators[i]] == operator:
            results[i] = operator(results[i], results[i+1])
            results.pop(i+1)
            operators.pop(i)
        else:
            i = i + 1
    return results

async def parseRollsCommand(message):
    command: str = message.content.lower()
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
    for character in commandInput:
        if possibleOperators.find(character) != -1:
            operators.append(character)
    results = await applyOperator(message, results, operators, pow)
    results = await applyOperator(message, results, operators, mul)
    results = await applyOperator(message, results, operators, truediv)
    results = await applyOperator(message, results, operators, mod)
    results = await applyOperator(message, results, operators, add)
    results = await applyOperator(message, results, operators, sub)
    
    await message.channel.send(f"Final results: {results}")