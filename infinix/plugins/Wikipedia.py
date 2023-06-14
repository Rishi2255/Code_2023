#from telethon.sync import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
import wikipedia
import re
from .. import bot
from telethon import events


@bot.on(events.NewMessage(incoming =True,pattern="/m (.*)"))
async def handle_new_message(event):
    if event.is_private:  # Only handle private messages
        message = event.message.message
        word = re.match("/m (.*)", message).group(1)

        try:
            page = wikipedia.page(word)
            summary = page.summary
            await event.reply(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            options = e.options[:5]  # Limit options to 5
            options_str = '\n'.join(options)
            await event.reply(f"Multiple options found. Please choose one:\n{options_str}")
        except wikipedia.exceptions.PageError:
            await event.reply("Couldn't find the requested word on Wikipedia.")

@bot.on(events.ChatAction)
async def handle_chat_action(event):
    if event.user_joined:
        await bot(JoinChannelRequest(event.chat_id)
