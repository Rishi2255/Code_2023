from telethon import events
from .. import bot,openai_key
import asyncio,openai


openai.api_key = openai_key


@bot.on(events.NewMessage(incoming = True, pattern ="(?i)/ask"))
async def _chatgpt(event):
  if event.sender_id == int(6129038868):
    await event.reply("Hello Rishika")
  else:
       await event.reply("Hello user")