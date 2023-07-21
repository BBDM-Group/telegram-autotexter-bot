from time import sleep
from threading import Thread

from pyrogram import Client, filters
from pyrogram.types import Message

from src.utils import *

CFG = get_cfg()

api_id = CFG['api_id']
api_hash = CFG['api_hash']

INTERVAL = 0.5

settings = get_settings()
app = Client(CFG['username'], CFG['api_id'], CFG['api_hash'])


@app.on_message(filters=filters.incoming & ~filters.group & ~filters.channel)
async def message_handler(client: Client, message: Message):
    await app.send_message(message.chat.id, settings['text_for_reply'])


def mail():
    for chat_ids in settings['ids']:
        app.send_message(chat_ids, settings['text'])
        sleep(INTERVAL)


def start_mailing():
    while True:
        if check_time(settings['timer']):
            print('Sending...')
            mail()
            new_timer = []
            for i in settings['timer']:
                new_timer.append(update_time(i, 7))
            update_settings('timer', new_timer)
        sleep(0.5)


def main():
    Thread(target=start_mailing).start()
    app.run()


if __name__ == '__main__':
    main()
