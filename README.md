# Telegram Planner
Telegram planner is a little application that performs posting of scheduled text messages to Telegram channels, so we can center our efforts in the content of the channels itself, and not that much in looking at the phone. This can be considered a productivity tool.

## Requirements
The program needs the _telethon_ python library to connect to Telegram. Also we need to place a secret json file called _telegram-planner.json_ in the directory _{root}/secret_, beinf root the Telegram Planner root directory. This json will have the following structure:

```
{
    "api_id": Integer with the secret API id provided by Telegram
    "api_hash": String with the secret API hash provided by Telegram,
    "posts_path": String with the path of the directory where the files to be sent will be stored
}
```

## Usage
In order to use the program, we must use the following command:

```
./telplan {command} {entity} [options]
```

The possible actions that can be performed are:

* Show all the channels where the user is owner:
```
./telplan show channels
```
* Show the posts thata are scheduled for a channel:
```
./telplan show calendar --channel {channel name}
```
* Add a single post to a channel (see considerations):
```
./telplan add post --channel {channel name} --text-path {file with the text of the post} --datetime {datetime}
```
* Add all the posts to a channel (see considerations):
```
./telplan add posts --channel {channel name}
```

## Considerations
* When we use datetime, the format must be _YYYYMMDD-HHmm_.
* When we use the _add posts_ command, the directory specified in the configuration json (see requeriments) will be used, and the text files inside the directory must have the format _YYYYMMDD-HHmm.txt_
