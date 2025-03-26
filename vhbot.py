from discord.ext import commands
import discord
from colorama import Fore
import vhconf as c
import asyncio

#NOTE : 'Members' intent must be enabled on your discord bot's page
#https://discordpy.readthedocs.io/en/latest/intents.html#privileged-intents
#https://discord.com/developers/applications
intents = discord.Intents.all()
intents.members = True

#bot = commands.Bot(command_prefix=[c.cmd_prefix, 'au ', 'Au '])
bot = commands.Bot(command_prefix='!', intents=intents)

extensions = ['cogs.raiseHand']


# if __name__ == '__main__':
#     for ext in extensions:
#         print(Fore.GREEN + "[STARTUP] : " + Fore.RESET + ext)
#         bot.load_extension(ext)

async def load_extensions():
    for ext in extensions:
        await bot.load_extension(ext)

@bot.command()
async def info(ctx):
    print("hi")
    await ctx.send(ctx.guild)

@bot.event
async def on_ready():
    print(Fore.GREEN + "[STARTUP] " + Fore.RESET +
        "Logged in as " + Fore.GREEN + bot.user.name + Fore.RESET)

async def main():
    async with bot:
        await load_extensions()
        await bot.start(c.token)

asyncio.run(main())

# bot.run(c.token)
