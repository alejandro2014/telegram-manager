from datetime import datetime, timedelta
import os

class PostsManager:
    def __init__(self, client, posts_path):
        self.client = client
        self.posts_path = posts_path

    async def add(self, args):
        channel_id = args.channel
        datetime = args.datetime
        text_path = f'{self.posts_path}/{args.datetime}.txt'

        with open(text_path, 'r') as f:
            text = f.read()

        entity = await self.client.get_entity(f'https://t.me/{args.channel}')
        timedelta = self.calculate_delta(args.datetime)

        await self.client.send_message(entity, text, schedule=timedelta)

    def calculate_delta(self, timestamp):
        year = int(timestamp[0:4])
        month = int(timestamp[4:6])
        day = int(timestamp[6:8])
        hour = int(timestamp[9:11])
        minute = int(timestamp[11:13])

        now = datetime.now()
        then = datetime(year, month, day, hour=hour, minute=minute)
        tdelta = then - now

        return tdelta
