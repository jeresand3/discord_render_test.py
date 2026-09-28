import os
import asyncio
import discord

print("DISCORD.PY VERSION:", discord.__version__)

import main

async def test():
    print("MAIN.PY IMPORTED")
    print("BOT OBJECT CREATED:", main.bot)
    print("INTENTS:", main.bot.intents)

    await main.bot.login(main.BOT_TOKEN)

    print("FULL MAIN.PY BOT LOGIN SUCCESS")

    await main.bot.close()

asyncio.run(test())
