from CalendarManager import CalendarManager
from ChannelsManager import ChannelsManager
from PostsManager import PostsManager

class ArgsParser:
    def __init__(self, client, posts_path):
        self.client = client
        self.posts_path = posts_path

        self.calendar_manager = CalendarManager(self.client)
        self.channels_manager = ChannelsManager(self.client)
        self.posts_manager = PostsManager(self.client, self.posts_path)

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
            self.check_param(args, 'channel')

            await self.calendar_manager.show(args.channel)
            self.exit_ok()

        self.exit_error(args)

    async def process_add(self, args):
        if args.subaction == 'post':
            self.check_param(args, 'channel')
            self.check_param(args, 'text_path', param_name_text='text-path')
            self.check_param(args, 'datetime')

            await self.posts_manager.add_post(args.channel, args.text_path, args.datetime)
            self.exit_ok()

        if args.subaction == 'posts':
            self.check_param(args, 'channel')

            await self.posts_manager.add_multiple_posts(args.channel)
            self.exit_ok()

        self.exit_error(args)

    def check_param(self, args, param_name, param_name_text=None):
        if not param_name_text:
            param_name_text = param_name

        if getattr(args, param_name) == None:
            print(f'ERROR: No --{param_name_text} specified')
            self.exit_error(args)

    def exit_ok(self):
        exit()

    def exit_error(self, args):
        print(f'Invalid action: {args.action}.{args.subaction}')
        exit(1)
