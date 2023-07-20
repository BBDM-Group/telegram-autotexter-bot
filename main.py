import asyncio
from time import sleep

from pyrogram import Client, filters

from src.utils import *

CFG = get_cfg()

api_id = CFG['api_id']
api_hash = CFG['api_hash']

INTERVAL = 0.5

app = Client(CFG['username'], CFG['api_id'], CFG['api_hash'])


@app.on_message(filters=filters.incoming & ~filters.group & ~filters.channel)
def log(client, message):
    print(message)


async def main():
    settings = get_settings()
    while True:
        if check_time(settings['timer']):
            print('Sending...')
            for chat_ids in settings['ids']:
                await app.send_message(chat_ids, settings['text'])
                sleep(INTERVAL)
            new_timer = []
            for i in settings['timer']:
                new_timer.append(update_time(i, 7))
            update_settings('timer', new_timer)
        sleep(0.5)


if __name__ == '__main__':
    app.run()
    asyncio.run(main())
