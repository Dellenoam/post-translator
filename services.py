import asyncio

from deep_translator import GoogleTranslator
from telethon import TelegramClient

from settings import API_HASH, API_ID, CHANNELS, SEND_TO_CHAT_ID

# Инициализация telegram client и google translator
client = TelegramClient("my_account", API_ID, API_HASH, system_version="4.16.30-vx3364")
translator = GoogleTranslator(source="auto", target="en")

# Последние посты для каждого канала
last_post_ids = {}
for channel in CHANNELS:
    last_post_ids.update({channel: None})


# Функция для получения постов из канала
async def get_posts(channel, last_post_id):
    async with client:
        if last_post_id is None:
            post = await client.get_messages(channel, limit=1)
            return post

        posts = await client.get_messages(channel, min_id=last_post_id, max_id=0)

        return posts[::-1]


# Функция для отправки постов в чат
async def send_to_channel(post, translated_text):
    async with client:
        # await client.forward_messages(SEND_TO_CHAT_ID, post)
        if translated_text:
            post.text = translated_text

        await client.send_message(SEND_TO_CHAT_ID, post.text)
        if post.media:
            await client.send_file(SEND_TO_CHAT_ID, post.media)


# Функция для обработки постов (перевод и отправка в чат)
async def google_translate(channel):
    posts = await get_posts(channel, last_post_ids[channel])

    for post in posts:
        try:
            post_text = post.text

            translated_text = None
            if post_text:
                translated_text = translator.translate(post_text)

            await send_to_channel(post, translated_text)

            last_post_ids[channel] = post.id

            await asyncio.sleep(1)
        except Exception as e:
            print(e)
