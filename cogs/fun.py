import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def neko(self, cxt):
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
    @commands.command()
    async def word(self, cxt, amount=1):
        f = open('words.txt')
        line = f.readlines()
        f.close
        last = len(line)-1
        rnd = random.randint(0, last)
        await cxt.send(line[rnd])

def setup(client):
    client.add_cog(Fun(client))