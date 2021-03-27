from datetime import datetime, timedelta
import os

class PostsManager:
    def __init__(self, client, posts_path):
        self.client = client
        self.posts_path = posts_path

    async def add_multiple_posts(self, channel_id):
        files = self.get_files_structure(self.posts_path)

        for file in files.keys():
            text_path = files[file]['txt']
            datetime = os.path.basename(text_path).split('.')[0]
            await self.add_post(channel_id, text_path, datetime)

    async def add_post(self, channel_id, text_path, datetime):
        with open(text_path, 'r') as f:
            text = f.read()

        entity = await self.client.get_entity(f'https://t.me/{channel_id}')
        timedelta = self.calculate_delta(datetime)

        print(f'----- Scheduling post for {datetime} / {timedelta}-----')
        print(text)
        await self.client.send_message(entity, text, schedule=timedelta)

    def get_files_structure(self, directory):
        files = {}

        for fname in os.listdir(directory):
            if fname != '.DS_Store' and (
                fname.endswith(".txt") or
                fname.endswith(".jpg") or
                fname.endswith(".pdf")
            ):
                fname_split = fname.split('.')
                timestamp = fname_split[0]
                extension = fname_split[1]

                if timestamp not in files:
                    files[timestamp] = {}

                files[timestamp][extension] = f'{directory}/{fname}'

        return files

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
