import discord
import time
import json

with open('config.json', 'r') as f:
    config = json.load(f)

client = discord.Client()
prevAuth = None
prevAuthNo = 0

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print(client.user.id)
    print('----READY----')

@client.event
async def on_message(message):

    global prevAuth
    global prevAuthNo

    if message.author == prevAuth:
        prevAuthNo = prevAuthNo + 1
        if prevAuthNo > 4:
            try:
                await client.delete_message(message)
            except Exception as e:
                print(e)
    else:
        prevAuthNo = 0

    if message.attachments or message.embeds:
        try:
            await client.delete_message(message)
        except Exception as e:
            print(e)

    if not message.content.lower() == config['letter']:
        try:
            await client.delete_message(message)
        except Exception as e:
            print(e)

    prevAuth = message.author

@client.event
async def on_message_edit(before, after):
    await client.delete_message(after)

client.run(config['token'])
