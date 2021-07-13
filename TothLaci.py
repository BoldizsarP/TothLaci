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
from datetime import datetime

TOKEN= os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(client.guilds)
    text_channels = client.guilds[0].text_channels
    channel = text_channels[0]
    # await channel.send("Szasztok skaccok")

@client.event
async def on_message(message):
    content = message.content
    channel = message.channel
    print(channel.type.value)
    if channel.type.value == 1:
        if content.split(' ')[0].isnumeric():
            time.sleep(int(content.split(' ')[0]))
            await message.reply(" ".join(content.split(' ')[1:]))
            
@client.event
async def on_member_update(old, new):
    pass


client.run(TOKEN)
