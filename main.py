import os
import ast
import asyncio
import time

import discord
from discord.ext import commands

import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='./storage/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

import math
import random

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

# cog shit
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
# more cog shit
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# purge
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def users(ctx):
    id = client.get_guild(697834161255219230)
    await ctx.send(f"""# of Members: {id.member_count}""")

# say
@client.command()
async def say(ctx, markup, *, txt):
    if markup == "bold":
        await ctx.send(f'**{txt}**')
    elif markup == "italic":
        await ctx.send(f"*{txt}*")
    elif markup == "strikethrough":
        await ctx.send(f"~~{txt}~~")
    elif markup == "underline":
        await ctx.send(f"__{txt}__")
    elif markup == 'all':
        await ctx.send(f'__~~***{txt}***~~__')
    elif markup == "code":
        await ctx.send(f'```{txt}```')
    elif markup == "everyone":
        await ctx.send(f'@everyone {txt}')
    else:
        await ctx.send(f'{markup} {txt}')

# random word
@client.command()
async def word(cxt, amount=1):
    f = open('words.txt')
    line = f.readlines()
    f.close
    last = len(line)-1
    rnd = random.randint(0, last)
    await cxt.send(line[rnd])

# neko 
@client.command()
async def neko(cxt):
    num = random.randint(1, 5)
    if num == 1:
        await cxt.send(file=discord.File('meme.png'))
    elif num == 2:
        await cxt.send(file=discord.File('nekoderp1.png'))
    elif num == 3:
        await cxt.send(file=discord.File('nekoderp2.jpg'))
    elif num == 4:
        await cxt.send(file=discord.File('nekofry.jpg'))
    elif num == 5:
        await cxt.send(file=discord.File('heilneko.png'))
    else:
        await cxt.send("try again pls (", num, ")" )

# calculator
@client.command()
async def calc(cxt, n1, operator, n2=0):
    if str(operator) == '+':
        await cxt.send(int(n1) + int(n2))
    elif str(operator) == '-':
        await cxt.send(int(n1) - int(n2))
    elif str(operator) == '*' or str(operator).upper() == 'X':
        await cxt.send(int(n1) * int(n2))
    elif str(operator) == '/':
        await cxt.send(int(n1) / int(n2))
    elif str(operator) == "pow":
        await cxt.send(pow(int(n1), int(n2)))
    elif str(operator) == "sqrt":
        await cxt.send(math.sqrt(int(n1)))

@client.command()
async def edned(cxt, one):
    if one == "1":
        homo = discord.Embed(title="AAAAAAAAAAAAAAA", type="rich", description="AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        homo.set_image(url="https://www.westlanders.nu/Content/Uploads/Nieuws%202017/Evenementen/DrPhil-1280x720px-Shareimage.jpg")
        await cxt.send(embed=homo)
    if one == "2":
        dieke = discord.Embed(title="AAAAAAAA", type="rich", description="heuj", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        await cxt.send(embed=dieke)

@client.command()
async def chc(cxt, *, name):
    guild = cxt.message.guild
    if ' ' in name:
        name.replace(" ", "-")
    await guild.create_text_channel(name)

@client.command()
async def chd(cxt, name):
    guild = cxt.message.guild
    await cxt.delete_channel(name)

client.run(token)