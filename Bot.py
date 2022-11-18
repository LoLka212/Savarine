import disnake
from disnake.ext import commands
import os

bot = commands.InteractionBot(intents=disnake.Intents.all())

@bot.slash_command(description="Replies with the given text!")
async def echo(
    inter: disnake.ApplicationCommandInteraction,
    text: str = commands.Param(description="Echo~"),
) -> None:
    await inter.response.send_message(text)

@bot.slash_command(description="Responds with 'World'")
async def hello(inter):
    await inter.response.send_message("World")

@bot.slash_command()
async def ping(inter,ctx, amount: int=None):
    await inter.response.send_message("Pong!")

bot.run(os.getenv('TOKEN'))
