import os
import discord
from keep_alive import keep_alive

TOKEN = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hi'):
        await message.channel.send('HI there!')

    if message.content.startswith('$GM'):
        await message.channel.send('Good Morning')    


keep_alive()
client.run(TOKEN)