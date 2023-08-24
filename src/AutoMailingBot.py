from errno import EL
import logging 
import random

from time import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from src.utils import *


logger = logging.getLogger(__name__)


CFG = get_cfg()

api_id = CFG['api_id']
api_hash = CFG['api_hash']


app = Client(CFG['username'], CFG['api_id'], CFG['api_hash'])


@app.on_message(filters=filters.incoming & ~filters.group & ~filters.channel & ~filters.bot)
async def message_handler(client: Client, message: Message):
    settings = get_settings()
    await app.send_message(message.chat.id, settings['text_for_reply'])


def mail():
    settings = get_settings()
    _chat_ids = [x.chat.id for x in app.get_dialogs() if (x.chat.id < 0 and x.chat.id not in settings['exclude_ids'])]
    
    amount_channels = settings.get('amount_channels', 0)
    amount_channels = len(_chat_ids) if (amount_channels > len(_chat_ids) or amount_channels == 0) else amount_channels
    
    _chat_ids_trimmed = []
    if amount_channels > 0 and amount_channels < len(_chat_ids):        
        for i in range(amount_channels):
            _id = random.choice([id for id in _chat_ids if id not in _chat_ids_trimmed])
            _chat_ids_trimmed.append(_id)
    else:
        _chat_ids_trimmed = _chat_ids          
    
    logger.info(f'list of chats: [{str(_chat_ids_trimmed)}]')
    print(f'list of chats: [{str(_chat_ids_trimmed)}]')

    # for chat_id in settings['ids']:
    for chat_id in _chat_ids_trimmed:
        try:
            print(f'Sending message to {chat_id}')
            app.send_message(chat_id, get_message_text(settings['text'], settings.get('error_depth', 1)))
            _sleep_time = get_sleep_time()
            print(f'sleeping for [{_sleep_time} sec]')
            sleep(_sleep_time)
        except Exception as e:
            print(f'Unable to send message: [{str(chat_id)}], error: [{e}]')
            logger.error(f'Unable to send message: [{str(chat_id)}], error: [{e}]')


def start_mailing():
    print("started sender app")

    while True:
        settings = get_settings()
        if check_time(settings['timer']):
            try:
                print(f'timer: [{settings["timer"]}]')
                print('trying to send messages')
                mail()
                new_timer = []
                for i in settings['timer']:
                    new_timer.append(update_time(i, 7))
                update_settings('timer', new_timer)
                print(f'new timer: [{settings["timer"]}]')
            except Exception as e: 
                logger.error(f'Something went wrong: [{e}]')
                print(f'Something went wrong: [{e}]')
        sleep(0.5)
