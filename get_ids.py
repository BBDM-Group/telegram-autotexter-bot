# Program-helper for obtaining IDs of chats
from pyrogram import Client

from src.utils import *

CFG = get_cfg()

api_id = CFG['api_id']
api_hash = CFG['api_hash']

INTERVAL = 0.5

app = Client(CFG['username'], CFG['api_id'], CFG['api_hash'])


def main():
    app.start()
    for dialog in app.get_dialogs():
        print(dialog.chat.first_name or dialog.chat.title, " has ID: ", dialog.chat.id)

main()
