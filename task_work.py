from pyrogram import Client
from decouple import config

bot = Client(name=config('LOGIN'),
             api_id=config('API_ID'),
             api_hash=config('API_HASH'),
             phone_number=config('PHONE'))

bot.start()

# Відправка повідомлення собі
bot.send_message(chat_id='me', text='Отправка сообщения себе')

# Відправка повідомлення за логіном
bot.send_message(chat_id='kroschu', text='Отправка сообщения по логину другому пользователю')

# Відправка повідомлення за Telegram ID
bot.send_message(chat_id=6412868393, text='Отправка сообщения по телеграмм айди')

# Відправка повідомлення в групу
bot.send_message(chat_id='-1002392775957', text='Отправка сообщения в приватную группу')

bot.stop()