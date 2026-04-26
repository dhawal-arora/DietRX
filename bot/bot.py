import discord
from discord.ext import commands
from config import COMMAND_PREFIX
from bot.commands import profile, diet, docs, misc


def create_bot():
    client = commands.Bot(command_prefix=[COMMAND_PREFIX], intents=discord.Intents.all())
    client.remove_command("help")

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")
        await client.wait_until_ready()
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name="/busreport")
        )
        await client.tree.sync()

    profile.setup(client)
    diet.setup(client)
    docs.setup(client)
    misc.setup(client)

    return client
