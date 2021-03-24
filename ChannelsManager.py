from TableFormatter import TableFormatter

from telethon.tl.types import Channel

class ChannelsManager:
    def __init__(self, client):
        self.client = client

    async def add(self):
        print('add-channel')

    async def delete(self):
        print('delete-channel')

    async def show(self):
        channels = []

        async for dialog in self.client.iter_dialogs():
            if isinstance(dialog.entity, Channel) and dialog.entity.creator and dialog.entity.broadcast:
                channels.append({
                    'name': dialog.name,
                    'id': str(dialog.id)
                })

        table_formatter = TableFormatter()
        table_formatter.print_table(channels)
