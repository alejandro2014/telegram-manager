from CalendarManager import CalendarManager
from ChannelsManager import ChannelsManager
from PostsManager import PostsManager

class ArgsParser:
    def __init__(self, client):
        self.client = client
        self.calendar_manager = CalendarManager(self.client)
        self.channels_manager = ChannelsManager(self.client)
        self.posts_manager = PostsManager(self.client)

    async def process_actions(self, args):
        if args.action == 'show':
            await self.process_show(args)
        elif args.action == 'add':
            await self.process_add(args)

    async def process_show(self, args):
        if args.subaction == 'channels':
            await self.channels_manager.show()
            self.exit_ok()

        if args.subaction == 'calendar':
            channel_id = args.channel

            if channel_id == None:
                print('ERROR: No channel id specified')
                self.exit_error(args)

            await self.calendar_manager.show(int(channel_id))
            self.exit_ok()

        self.exit_error(args)

    async def process_add(self, args):
        if args.subaction == 'post':
            if args.channel == None:
                print('ERROR: No --channel specified')
                self.exit_error(args)

            if args.id == None:
                print('ERROR: No message id specified')
                self.exit_error(args)

            if args.datetime == None:
                print('ERROR: No datetime specified')
                self.exit_error(args)

            await self.posts_manager.add(args)
            self.exit_ok()

        self.exit_error(args)

    def exit_ok(self):
        exit()

    def exit_error(self, args):
        print(f'Invalid action: {args.action}.{args.subaction}')
        exit(1)
