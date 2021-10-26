# import os

# import discord

# TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()

# @client.event
# async def on_member_join():
#     print(f'{client.user} has connected to Discord!')

# client.run(TOKEN)
import discord
import time
import os

from discord.message import Message
from masik import printer as print
from kikerdezo import kvizkerdeskezelo
from datetime import datetime

TOKEN= os.getenv("DISCORD_TOKEN",'ODYzMDk5MzM4OTAwNjM1Njg4.YOh95g.Y3q7hay4yvCE-_IEKBv67Sz34QM')

client = discord.Client()

@client.event
async def on_ready():
    print(client.guilds)
    text_channels = client.guilds[0].text_channels
    channel = text_channels[0]
    # await channel.send("Szasztok skaccok")

@client.event
async def on_message(message):
    if message.reference:
        pass
    if message.content == '!kvizkerdesek':
        kvizkerdeskezelo()

    content = message.content
    channel = message.channel
    print(channel.type.value)
    if channel.type.value == 1:
        if content.split(' ')[0].isnumeric():
            time.sleep(int(content.split(' ')[0]))
            await message.reply(" ".join(content.split(' ')[1:]))

@client.event
async def on_member_join(member):
    pass
            
@client.event
async def on_member_update(old, new):
    pass


client.run(TOKEN)
