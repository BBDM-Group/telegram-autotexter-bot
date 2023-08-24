import json
import random

from datetime import datetime, timedelta
from typing import List, Any


def get_cfg():
    with open('config.json') as f:
        return json.load(f)


def get_settings():
    with open('settings.json', encoding='utf-8') as f:
        return json.load(f)


def update_settings(key_to_update, new_content):
    with open('settings.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    if isinstance(content.get(key_to_update), list) and key_to_update == 'text':
        content[key_to_update].append(new_content)
    else:
        content[key_to_update] = new_content
    with open('settings.json', 'w') as f:
        json.dump(content, f, indent=4)


def check_time(time):
    return str(datetime.strftime(datetime.now(), '%d-%m-%y %H:%M:%S')) in time


def update_time(time, new_time):
    old_time = datetime.strptime(time, '%d-%m-%y %H:%M:%S')
    return datetime.strftime(old_time + timedelta(days=new_time), '%d-%m-%y %H:%M:%S')


def get_sleep_time():
    return random.randrange(300, 600)


def get_message_text(lst_messages: List[str], error_depth: int = 1) -> str:
    _str_message = random.choice(lst_messages)
    message = _str_message
    for i in range(error_depth):
        message = _get_message_text(message)
    return message


def _get_message_text(_str_message: str) -> str:
    _rnd_modifier = random.randint(0, len(_str_message))
    
    message = _str_message[:_rnd_modifier] + f'{random.randint(0,5)}' + _str_message[_rnd_modifier:]
    message = message + '.' if _rnd_modifier/2 == int(_rnd_modifier/2) else message + ',.'
    message = ' ' + message if _rnd_modifier/2 == int(_rnd_modifier/2) else message
    return message