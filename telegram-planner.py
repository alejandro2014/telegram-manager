import json

from telethon import TelegramClient
from telethon.tl.types import Channel

from TableFormatter import TableFormatter

with open('secret/telegram-planner.json') as f:
    secret_values = json.load(f)

api_id = secret_values['api_id']
api_hash = secret_values['api_hash']
client = TelegramClient('anon', api_id, api_hash)

async def main():
    rows_info = []

    async for dialog in client.iter_dialogs():
        if isinstance(dialog.entity, Channel) and dialog.entity.creator and dialog.entity.broadcast:
            rows_info.append({
                'name': dialog.name,
                'id': str(dialog.id)
            })

    table_formatter = TableFormatter()
    table_formatter.print_table(rows_info)

with client:
    client.loop.run_until_complete(main())

exit()

import argparse

from ArgsParser import ArgsParser

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('action')
    parser.add_argument('subaction')

    return parser

args_parser = ArgsParser()

parser = create_parser()
args = parser.parse_args()

args_parser.process_actions(args)
