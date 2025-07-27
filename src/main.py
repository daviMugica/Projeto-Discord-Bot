import discord
from discord import app_commands
from dotenv import load_dotenv
import os

load_dotenv(override=True)
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX")


class Bot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix = BOT_PREFIX,
            intents = intents
        )
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O {self.user} foi ligado!")


bot = Bot()

bot.run(DISCORD_TOKEN)
