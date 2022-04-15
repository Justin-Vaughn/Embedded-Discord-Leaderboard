import datetime

import discord
from discord.ext import commands, tasks
from HypixelAPI import *

TOKEN = "TOKEN"
client = commands.Bot(command_prefix = ";")
print("Bot is loading...")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def gxp(ctx):
    embed = discord.Embed(
        color = discord.Colour.from_rgb(255, 153, 0),
        title = ":crown:  Collusion GXP  :crown:",
        description= f"`Total Guild XP:`\n{totalGXP()}"

    )
    leaderboards = formatedList()
    date = datetime.date.today()-datetime.timedelta(days=1)
    embed.add_field(name=f"**[{date}]**", value=leaderboards, inline=False)

    embed.set_footer(text="Bot by Justin#3869")

    await ctx.send(embed = embed)


client.run(TOKEN)