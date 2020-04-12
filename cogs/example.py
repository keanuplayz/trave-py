import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('nigggEEEER')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong nigga")

def setup(client):
    client.add_cog(Example(client))