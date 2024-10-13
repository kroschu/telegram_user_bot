from pyrogram import Client, filters
from decouple import config
from pyrogram.types import Message
from datetime import datetime
import pytz

# Инициализация клиента
bot = Client(name=config('LOGIN'),
             api_id=config('API_ID'),
             api_hash=config('API_HASH'),
             phone_number=config('PHONE'))

# Обработчик входящих сообщений
@bot.on_message(filters.text)
async def handle_message(client: Client, message: Message):
    text = message.text.lower()

    # Пересылка сообщения в чат с ID 7570742964
    try:
        await client.forward_messages(
            chat_id="7570742964",
            from_chat_id=message.chat.id,
            message_ids=message.id
        )
        print(f"Сообщение переслано в чат с ID 7570742964: {message.text}")
    except Exception as e:
        print(f"Ошибка при пересылке сообщения: {e}")

# Запуск клиента
bot.run()