import argparse
import json

from telethon import TelegramClient, functions, types

from ArgsParser import ArgsParser

with open('secret/telegram-planner.json') as f:
    secret_values = json.load(f)

api_id = secret_values['api_id']
api_hash = secret_values['api_hash']
client = TelegramClient('anon', api_id, api_hash)

def create_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('action')
    parser.add_argument('subaction')
    parser.add_argument('--channel', dest='channel', required=False, default=None,
        help='Name of the channel to be used')
    parser.add_argument('--datetime', dest='datetime', required=False, default=None,
        help='Datetime for publishing the post (format YYYY-MM-DD HH:MM)')
    parser.add_argument('--id', dest='id', required=False, default=None,
        help='Name of the resources to be added (txt, png and pdf)')

    return parser

args_parser = ArgsParser(client)
parser = create_parser()
args = parser.parse_args()

async def main():
    await args_parser.process_actions(args)

with client:
    client.loop.run_until_complete(main())
