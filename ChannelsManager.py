from TableFormatter import TableFormatter

from telethon.tl.types import Channel

class ChannelsManager:
    def __init__(self, client):
        self.client = client

    async def show(self):
        channels = []

        async for dialog in self.client.iter_dialogs():
            if isinstance(dialog.entity, Channel) and dialog.entity.creator and dialog.entity.broadcast:
                channels.append({
                    'name': dialog.name,
                    'id': str(dialog.entity.id),
                    'id-text': dialog.entity.username if dialog.entity.username else '-'
                })

        table_formatter = TableFormatter()
        table_formatter.print_table(channels)
