# <b>REXER</b>
![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=welcome+To+REXER!;created+by+ZINAN+TECH+2+.O!;A+simple+autofilter+Bot!;Auto+filter+with+double+button!;start+message+with+pic!;and+all+other+features!)
 ⚚ ℭ𝔩𝔦𝔠𝔨 𝔗𝔥𝔢 ℑ𝔪𝔞𝔤𝔢 𝔗𝔬 𝔇𝔢𝔭𝔩𝔬𝔶 𝔜𝔬𝔲𝔯 𝔄𝔭𝔭 ⚚


[![Deploy](https://telegra.ph/file/37d5862e978b6aaeb1b37.jpg)](https://heroku.com/deploy?template=https://github.com/Zinan100/REXER)

- [x] Auto Filter
- [x] Manuel Filter
- [x] IMDB
- [x] Admin Commands
- [x] Broadcast
- [x] Index
- [x] IMDB search
- [x] Fun mode
- [x] Inline Search
- [x] Random pics
- [x] ids and User info 
- [x] Stats, Users, Chats, Ban, Unban, Leave, Disable, Channel



<h3 align="center">ℂ𝕆ℕ𝕋𝔸ℂ𝕋<img align="center" src="https://github.com/Aadhi000/Adv-Ajax/blob/main/assets/Handshake.gif" height="33px" /></h3>
<p align="center">
<a href="https://t.me/zinan00100"><img alt="Telegram" src="https://img.shields.io/badge/𝙳𝙴𝚅 1-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/></a>
<a href="https://t.me/albintko"><img alt="Telegram" src="https://img.shields.io/badge/𝙳𝙴𝚅 2-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/></a>
</p>



## Installation

















## DEPLOY ON HEROKU
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Zinan100/REXER)


#Hard Way

```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
env\Scripts\activate.bat # For Windows
source env/bin/activate # For Linux or MacOS

# Install Packages
pip3 install -r requirements.txt

# Edit info.py with variables as given below then run bot
python3 bot.py
```
Check [`sample_info.py`](sample_info.py) before editing [`info.py`](info.py) file

## Variables

### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). For more help watch this [video](https://youtu.be/1G1XwEOnxxo)
* `LOG_CHANNEL` : A channel to log the activities of bot. Make sure bot is an admin in the channel.
### Optional Variables
* `PICS`: Telegraph links of images to show in start message.( Multiple images can be used seperated by space )
* Check [info.py](https://github.com/EvamariaTG/evamaria/blob/master/info.py) for more

## Note
* Currently the [API used](http://www.omdbapi.com) in this repo is allowing 1000 requests per day. [You may not get posters if its crossed](https://t.me/ThankTelegram/910168). 
Once a poster is fetched from OMDB , poster is saved to DB to reduce duplicate requests.

## Admin commands
```
channel - Get basic infomation about channels
total - Show total of saved files
delete - Delete file from database
index - Index all files from channel.
logger - Get log file
```

## Tips
* You can use `|` to separate query and file type while searching for specific type of file. For example: `Avengers | video`
* If you don't want to create a channel or group, use your chat ID / username as the channel ID. When you send a file to a bot, it will be saved in the database.



## Thanks to 
* [Pyrogram](https://github.com/pyrogram/pyrogram)
* Original [Repo](https://github.com/Aadhi000/Ajax)
