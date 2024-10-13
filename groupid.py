from pyrogram import Client
from decouple import config

bot = Client(name=config('LOGIN'),
             api_id=config('API_ID'),
             api_hash=config('API_HASH'),
             phone_number=config('PHONE'))

bot.start()

# Отримати останнє повідомлення з групи
messages = bot.get_chat_history(chat_id="Obsidian inbox indposhyv", limit=1)

for message in messages:
    print(message.chat.id)  # Виведе chat_id групи

bot.stop()