import discord
from discord.ext import commands
import math

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calc(self, cxt, n1, operator, n2=0):
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
    
    @commands.command()
    async def say(self, ctx, markup, *, txt):
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

    @commands.command()
    async def users(self, ctx):
        id = client.get_guild(697834161255219230)
        await ctx.send(f"""# of Members: {id.member_count}""")

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def chc(self, cxt, *, name):
        guild = cxt.message.guild
        if ' ' in name:
            name.replace(" ", "-")
        await guild.create_text_channel(name)

    @commands.command()
    async def chd(self, cxt, name):
        guild = cxt.message.guild
        await cxt.delete_channel(name)


def setup(client):
    client.add_cog(Utility(client))