from CalendarManager import CalendarManager
from ChannelsManager import ChannelsManager
from PostsManager import PostsManager

class ArgsParser:
    def __init__(self, client):
        self.client = client
        self.calendar_manager = CalendarManager()
        self.channels_manager = ChannelsManager(self.client)
        self.posts_manager = PostsManager()

    async def process_actions(self, args):
        if args.action == 'show':
            await self.process_show(args)
        elif args.action == 'add':
            await self.process_add(args)
        elif args.action == 'delete':
            await self.process_delete(args)

    async def process_show(self, args):
        if args.subaction == 'channels':
            await self.channels_manager.show(self.client)
            self.exit_ok()

        if args.subaction == 'post':
            await self.posts_manager.show()
            self.exit_ok()

        if args.subaction == 'calendar':
            await self.calendar_manager.show()
            self.exit_ok()

        self.exit_error(args)

    async def process_add(self, args):
        if args.subaction == 'post':
            await self.posts_manager.add()
            self.exit_ok()

        if args.subaction == 'channel':
            await self.channels_manager.add()
            self.exit_ok()

        self.exit_error(args)

    async def process_delete(self, args):
        if args.subaction == 'post':
            await self.posts_manager.delete()
            self.exit_ok()

        if args.subaction == 'channel':
            await self.channels_manager.delete()
            self.exit_ok()

        self.exit_error(args)

    def exit_ok(self):
        exit()

    def exit_error(self, args):
        print(f'Invalid action: {args.action}.{args.subaction}')
        exit(1)
