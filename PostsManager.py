class PostsManager:
    def __init__(self, client):
        self.client = client

    async def add(self):
        print('add-post')

    async def delete(self):
        print('delete-post')

    async def show(self):
        print('show-post')
