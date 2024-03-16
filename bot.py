"""
SheetBot setup and main functions
"""

import logging
import os
import discord
from discord import File
from discord.ext import commands
from dotenv import load_dotenv
import main

logger = logging.getLogger(__name__)
load_dotenv()
TOKEN = os.getenv("TOKEN")


def run():
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        logging.info("User: %s", bot.user)

    @bot.command(name="LoadMain")
    async def loadmain(ctx):
        main.getdata("#2PRJY9QY9")
        main.updatesheet()
        file_name = "CWL2024.xlsx"

        await ctx.send("**CWL 2024 Season**")
        await ctx.send(
            "Updated: "
            + main.warsL[0]["startTime"][4:6]
            + "-"
            + main.warsL[0]["startTime"][0:4]
        )
        await ctx.send(file=File(file_name))

    bot.run(TOKEN)


if __name__ == "__main__":
    run()
