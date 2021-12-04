import discord
import os
from src import ideation_source, time_handler, keep_alive, daily_message
from replit import db

client = discord.Client()
daily_channel_id = 916626227123593256 # Channel 'Daily'
db["timezone"] = "EET"  # Finland Time Zone (UTC+02:00)
db["daily_time"] = "06:00:00"

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

  daily_message.msg1.start(client, daily_channel_id) #start daily message

#handle incoming command from user
@client.event
async def on_message(message: discord.Message) -> None:
  if message.author == client:
    return
  msg = message.content

  #random ideation source
  if msg.startswith("$word"):
    await message.channel.send(ideation_source.get_word_idea_or_sentence("mot"))

  if msg.startswith("$idea"):
    await message.channel.send(ideation_source.get_word_idea_or_sentence("idee"))
  
  if msg.startswith("$sentence"):
    await message.channel.send(ideation_source.get_word_idea_or_sentence("phrase"))

  #time
  if msg.startswith("$time"):
    await message.channel.send(time_handler.get_current_time(db["timezone"]))
  
  if msg.startswith("$settime"):
    db["timezone"] = msg.split("$settime ",1)[1]
    await message.channel.send("Timezone \"{0}\" successfully set.".format(db["timezone"]))

  #TODO:
  #clean handler_cmd
  #commands: set_daily_time, set_daily_channel_id and help

keep_alive.keep_alive()
client.run(os.environ["TOKEN"])
