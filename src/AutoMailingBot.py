from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from src.utils import *

CFG = get_cfg()

api_id = CFG['api_id']
api_hash = CFG['api_hash']

INTERVAL = 0.5

app = Client(CFG['username'], CFG['api_id'], CFG['api_hash'])


@app.on_message(filters=filters.incoming & ~filters.group & ~filters.channel & ~filters.bot)
async def message_handler(client: Client, message: Message):
    settings = get_settings()
    await app.send_message(message.chat.id, settings['text_for_reply'])


def mail():
    settings = get_settings()
    for chat_id in settings['ids']:
        print(f'Sending message to {chat_id}')
        app.send_message(chat_id, settings['text'])
        sleep(INTERVAL)


def start_mailing():
    while True:
        settings = get_settings()
        if check_time(settings['timer']):
            mail()
            new_timer = []
            for i in settings['timer']:
                new_timer.append(update_time(i, 7))
            update_settings('timer', new_timer)
        sleep(0.5)
