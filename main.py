import discord
import os
from creative_api import get_idea
from keep_alive import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return

  if message.content.startswith("$idea"):
    idea = get_idea()
    await message.channel.send(idea)

keep_alive()
client.run(os.environ['TOKEN'])