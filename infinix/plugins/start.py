from .. import bot
from telethon import events
import asyncio







@bot.on(events.NewMessage(incoming= True,pattern="/start"))
async def start(event):
  await  event.reply("Hello this is infinix bot")

@bot.on(events.NewMessage(incoming= True,pattern="/get"))
async def start(event):
  await  event.reply("Hello this is get command")
  
@bot.on(events.NewMessage(incoming= True,pattern="/eval"))
async def start(event):
  await  event.reply("Hello this is eval command")
  
@bot.on(events.NewMessage(incoming= True,pattern="/hello"))
async def start(event):
  await  event.reply("Hello this is hello command")
 
@bot.on(events.NewMessage(incoming= True,pattern="/star"))
async def start(event):
  a = await  event.reply("Hello 🦋")
  await asyncio.sleep(2)
  await a.edit("Hii 🌸")
