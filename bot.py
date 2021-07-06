# Autobump Selfbot
# Read the readme.md for detais on setting up
import discord
from discord.ext import commands
import asyncio
import datetime
import time

c = commands.Bot(command_prefix=';', self_bot=False, reconnect=True, status=discord.Status.idle)
c.remove_command('help')
token = open("config/token.txt").read()

@c.event
async def on_ready():
    print(f'{c.user} is logged in')
    pass

@c.event
async def on_message(ctx, limit=1):
    if ctx.author.id == 735147814878969968:
        await ctx.channel.trigger_typing()
        await asyncio.sleep(3)
        await ctx.channel.send('!d bump')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=limit)
        pass
    pass
        
c.run(token, bot=False)
