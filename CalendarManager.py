from telethon import functions

from TableFormatter import TableFormatter

class CalendarManager:
    def __init__(self, client):
        self.client = client

    async def show(self, group_id):
        result = await self.client(functions.messages.GetScheduledHistoryRequest(
            peer=group_id,
            hash=0
        ))

        messages = result.messages
        processed_messages = []

        for message in messages:
            processed_messages.append({
                'date': str(message.date)[:16],
                'message': message.message[:60].replace('\n', ' ')
            })

        table_formatter = TableFormatter()
        table_formatter.print_table(processed_messages)
