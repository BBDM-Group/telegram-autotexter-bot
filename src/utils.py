import json
from datetime import datetime, timedelta


def get_cfg():
    with open('config.json') as f:
        return json.load(f)


def get_settings():
    with open('settings.json', encoding='utf-8') as f:
        return json.load(f)


def update_settings(key_to_update, new_content):
    with open('settings.json', 'r', encoding='utf-8') as f:
        content = json.load(f)
    content[key_to_update] = new_content
    with open('settings.json', 'w') as f:
        json.dump(content, f)


def check_time(time):
    return str(datetime.strftime(datetime.now(), '%d-%m-%y %H:%M:%S')) in time


def update_time(time, new_time):
    old_time = datetime.strptime(time, '%d-%m-%y %H:%M:%S')
    return datetime.strftime(old_time + timedelta(days=new_time), '%d-%m-%y %H:%M:%S')
