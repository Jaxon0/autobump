Message From Dev
------------------------------------------------
This project is currently on hold due to the shutdown of discord.py. Soon, I plan to migrate the project to Hikari (another python discord wrapper). Please use this with caution as it is unsafe and has privacy holes.

# Discord - Autobump
Sexy discord autobump that will automatically bump your server, then delete the last 2 messages in an attempt to be secretive.

### Useless Information:
- Written in Discord.py
- Useful ngl

## Setup Instructions
Python 3.8 or higher required
### Dependencies
- Discord.py
- A server to run it on
- A (hopefully alt) discord account

### Installation

Start with installing Discord.py

```pip3 install discord.py```

Now, clone the repo

```gh repo clone Jaxon0/autobump```

Now you need to set everything up.
- Navigate to the config folder
- Go to token.txt
- Paste your token for your account
- Please make sure the bot user has delete messages permission on the server

**How Do I Get My Account Token?**

- Open discord in the browser
- Open developer tools > application > local storage > https://discord.com > scroll all the way to the bottom and refresh, make sure to copy it quickly
- **WHEN PASTING UR TOKEN INTO THE FILE MAKE SURE TO TAKE OUT THE QUOTATIONS

### Making it work
- Add [this bot](https://discord.com/oauth2/authorize?client_id=735147814878969968&permissions=268696721&scope=applications.commands%20bot)

**Setup The Bot**

Set the channel

```%setup add <#channel>```

*i reccommend making it in a private channel, to avoid users spamming the bot if they catch on that its a autobump*

Add your selfbot user to the bump remind

```%setup ping @account```

Now, start the bot, and you should be set!

# NOTICE:

```
SelfBots are against Discord TOS, and against Disboard TOS. I do not reccommend you use this as you could get your account banned/terminated. I am not responsible for terminated accounts and do not condone the use of this.
```
