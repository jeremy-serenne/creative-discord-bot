import asyncio
from discord.ext import tasks
from src.ideation_source import get_daily_ideation
from src.time_handler import get_current_time
from replit import db

@tasks.loop(hours=24)
async def msg1(client, daily_channel_id: int) -> None:
  await client.get_channel(daily_channel_id).send("@everyone\nDaily: "+get_daily_ideation())

@msg1.before_loop
async def before_msg1() -> None:
  while 1:  # loop the whole day
      if get_current_time(db["timezone"]) == db["daily_time"]:  # 24 hour format
          return
      await asyncio.sleep(1)
