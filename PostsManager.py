import os

class PostsManager:
    def __init__(self, client):
        self.client = client
        self.base_path = '~/Desktop/telegram-posts'

    async def add(self, args):
        channel_id = args.channel
        message_id = args.id
        datetime = args.datetime

        text_path = f'{self.base_path}/{message_id}.txt'

        if not os.path.isfile(text_path):
            print(f"ERROR: There is no text file ({text_path})")
            return

        print(f'Channel id: {channel_id}')
        print(f'Message id: {message_id}')
        print(f'Datetime: {datetime}')
