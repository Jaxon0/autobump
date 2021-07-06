# Autobump Selfbot
# Read the readme.md for detais on setting up
import discord
from discord.ext import commands
import asyncio

c = commands.Bot(command_prefix=';', self_bot=False, reconnect=True, status=discord.Status.idle)
c.remove_command('help')
token = open("config/token.txt").read()

@c.event
async def on_ready():
    print(f'{c.user} is logged in')
    pass

@c.event
async def on_message(ctx):
    if ctx.author.id == 735147814878969968:
        await ctx.channel.trigger_typing()
        await asyncio.sleep(3)
        await ctx.channel.send('!d bump')
        pass
    pass

        
c.run(token, bot=False)
