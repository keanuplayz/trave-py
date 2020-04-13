# Important packages
import os
import ast
import asyncio
import time

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

# Dotenv
import dotenv
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix = "t!")

# on_ready event
@client.event
async def on_ready():
    print("Ready!")
    print("Logged in as:", client.user.name, "(", client.user.id, ")")

@client.event
async def on_member_join(self, member):
    ment = member.mention
    await self.client.get_channel(697834161762861078).send(f"{ment} has joined the server.")
    print(f"{member} has joined the server.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)