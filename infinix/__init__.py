from telethon import TelegramClient 
import logging
import time


openai_key = "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"

api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6147733592:AAF_WIb8uXn95UAOZiiCY3xgdB1Pc2VYTLQ"

bot = TelegramClient("infinix",api_id,api_hash).start(bot_token = bot_token)



