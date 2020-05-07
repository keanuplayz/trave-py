# Important packages
import os
import ast
import asyncio
import time

# Uptime command
import psutil
pid = psutil.Process(os.getpid())
pid.create_time()
uptime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(pid.create_time()))

# Discord
import discord
from discord.ext import commands

# Logging
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./storage/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Command-required packages
import math
import random
import json

# Dotenv
import dotenv
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

def get_prefix(client, message):
    with open('./storage/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = get_prefix)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# on_ready event
@client.event
async def on_ready():
    print("Ready!")
    print("Logged in as:", client.user.name, "(", client.user.id, ")")

@client.event
async def on_guild_join(guild):
    with open('./storage/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(guild.id)] = 't!'

    with open('./storage/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('./storage/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes.pop(str(guild.id))

    with open('./storage/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments.')
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('This command does not exist. Use `.help` to view all available commands.')
    

@client.command()
async def cprefix(ctx, prefix):
    with open('./storage/prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open('./storage/prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix changed to: {prefix}')

@client.command()
async def uptime(ctx):
    await ctx.send(uptime)

@client.event
async def on_member_join(self, member):
    ment = member.mention
    await self.client.get_channel(697834161762861078).send(f"{ment} has joined the server.")
    print(f"{member} has joined the server.")

client.run(token)