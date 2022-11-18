import disnake
from disnake.ext import commands
import os

bot = commands.InteractionBot(intents=disnake.Intents.all())

@bot.slash_command()
async def ping(inter,ctx, amount: int=None):
    await inter.response.send_message("Pong!")

bot.run(os.getenv('TOKEN'))
