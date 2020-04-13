import discord
from discord.ext import commands

class System(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Change status
    @commands.command()
    async def status(self, ctx, status):
        if status == "online":
            await client.change_presence(status=discord.Status.online)
            ctx.send("Status changed to online.")
        if status == "idle":
            await client.change_presence(status=discord.Status.idle)
            ctx.send("Status changed to idle.")
        if status == "dnd":
            await client.change_presence(status=discord.Status.dnd)
            ctx.send("Status changed to do not disturb.")
        if status == "invis":
            await client.change_presence(status=discord.Status.invisible)
            ctx.send("Status changed to invisible.")

    # cog shit
    @commands.command()
    async def load(self, ctx, extension):
        client.load_extension(f'cogs.{extension}')
    # more cog shit
    @commands.command()
    async def unload(self, ctx, extension):
        client.unload_extension(f'cogs.{extension}')

def setup(client):
    client.add_cog(System(client))