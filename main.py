#prefix for bot is "!", you can change it on the PREFIX variable right under the imports

import discord

from discord.ext import commands

TOKEN = "place your token here"
PREFIX = "!"
BOT_CHANNEL = 123123123123 # main bot channel id

client = commands.Bot(command_prefix=PREFIX, case_insensitive=True)

@client.event()
async def on_ready():
    print("Bot ready")
    bot_channel = client.get_channel(BOT_CHANNEL)
    bot_latency = round(client.latency*1000)
    embed = discord.Embed(title="Bot is ready",
                          description="Bot is online and ready to be used",
                          colour=0x218a3d)
    embed.add_field(name="Latency",
                    value=f"{bot_latency}ms",
                    inline=True)
    bot_channel.send(embed=embed)

client.run(TOKEN)
