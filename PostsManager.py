class PostsManager:
    def __init__(self, client):
        self.client = client

    async def add(self, args):
        channel_id = args.channel
        message_id = args.id
        datetime = args.datetime
