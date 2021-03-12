# The infamous Merguezobot

It's a simple Discord bot to print infos from Monoplanete website on command

## Usage 

For now only one command is available : 

> !merguez [name of bike] [optional year model]

example :

> !merguez FZR 1000 1992

will return the data

Another feature is a random message sent in reply with a 1/10 appearing chance when someone sends a link to a motorcycle from Leboncoin.

## Installation 

### Guides

Just like any other bot you can follow this guide : https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-bot

Hosting it for free on Heroku : https://www.techwithtim.net/tutorials/discord-py/hosting-a-discord-bot-for-free/

### Configuration

You must have the `MERGUEZ_DISCORD_SECRET_KEY` environment variable to be set 

To disable showing more informations than the motoplanete link you must set the `MERGUEZ_DISABLE_DETAILS` environment variable to `true`

You can set your own command with the `MERGUEZ_COMMAND` environment variable (defaults to `!merguez`)

### Run the bot

You must first install the requirements

> pip install -r requirements.txt

Then simply run the bot

> python bot.py
