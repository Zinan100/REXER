class script(object):
    START_TXT = """π·π΄π»πΎ {},
πΌπ’ ππππ , <a href='https://t.me/Rexer0BOT_BOT'>πππππ</a>, πΈπ'π ππππ’ ππππ’ ππππ πππ ππ ππ π’πππ πππππ πππ ππππ ππ πππππ, πππππ πππ πΈ'ππ πππππππ ππππππ πππππ β₯οΈ
π°πΎππππππ π»π πππ πππππ ππ π€πΆπ»π» π°"""
    HELP_TXT = """ ΰ΄¦ΰ΄Ύ ΰ΄ͺΰ΄Ώΰ΄ΰ΄Ώΰ΄ΰ΅ΰ΄ΰ΅ ."""
    ABOUT_TXT = """
βββββββββββββββββββββββββββββββββ
βββββββ° REXER β±βββͺΌπ
ββ­ββββββββββββββββ€ΝΝΝΝβ 
ββ£βͺΌ πΌπ π½π°πΌπ΄ - <a href="https://t.me/Rexer0BOT_BOT> REXER </a>
ββ£βͺΌ π²ππ΄π°ππΎπ - <a href="https://t.me/zinan00100"> ZINAN TECH 2.O</a>
ββ£βͺΌ π»πΈπ±ππ°ππ - πΏπππΎπΆππ°πΌ
ββ£βͺΌ π»π°π½πΆππ°πΆπ΄ - πΏπππ·πΎπ½ πΉ
ββ£βͺΌ π³π°ππ°π±π°ππ΄ - πΌπΎπ½πΆπΎ π³π±
ββ£βͺΌ ππ΄πππ΄π -  π·π΄ππΎπΊπ
ββ£βͺΌ π±ππΈπ»π πππ°ππ - v1.0.2 [ π±π΄ππ° ]
ββ°ββββββββββββββββ€ΝΝΝΝβ ββββββββββββββββββββͺΌπ"""
    SOURCE_TXT = """<b>NOTE:</b>
- π° ππ  π ππππ ππππππ πππππππ. 
- ΥOαααα΄ αOαͺα΄ - <a href="https://github.com/Lallu-lallus/AnnaBen_robot"> πππππ πππ₯π </a>

π ππ¦π§ππ₯:
<a href="https://t.me/team_annaben"> π»π¬π¨π΄ π¨π΅π΅π¨ </a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details

β’/whois :-give a user full details"""
    ALIVE_TXT ="""<b>ALIVE MODULE</b>
β’ /alive - check me alive or deadπ"""
    CORONA_TXT ="""<b>Here is the help for the coron information module</b>
β‘οΈ /covid <code>(countryname)</code> <b>you can find a corona information of every country</b>

β‘οΈ <b>example</b> : - /covid India"""
    STICKER_TXT ="""<b>COMMAND /stickerid\nπ¨πΏ πΈππ π­πΎπΎπ½ π³πΎππΎπππΊπ π²πππΌππΎπ π¨π½ π’πππΌπ /stickerid π³π π¦πΎπ π²πππΌππΎπ π¨π½ (π±πΎπππ πΆπππ π²πππΌππΎπ)</b>"""
    SONG_TXT ="""<b>SONG MODULE</b>
Song Download
Song Download Module, For Those Who Love Music

π Command

β’ /song or /mp3 (songname) - download song from yt servers.
β’ /video or /mp4 (songname) - download video from yt servers

Usage
- working pm and groups"""
    JSON_TXT ="""<b>JSON MODULE</b>
JSON:
Bot returns json for all replied messages with /json

Features:
Message Editting JSON
Pm Support
Group Support

Note:
Everyone can use this command , if spaming happens bot will automatically ban you from the group"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>π Commands & Usage:</b>

β /Pin :- Pin The Message You Replied To Message To Send A Notification To Group Members

β /Unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    FUN_TXT ="""<b>FUN MODULE</b> 
    
<b>π² NOTHING MUCH JUST SOME FUN THINGS</b>
tππ ππππ π?ππ: 
π£. /dice - Roll The Dice 
π€. /Throw ππ /Dart - π³π π¬πΊππΎ Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUALFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Dingdi will respond whenever a keyword is found the message

<b>NOTE:</b>
1. IMDb should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - add a filter in chat.
β’ /filters - list all the filters of a chat.
β’ /del - delete a specific filter in chat.
β’ /delall - delete the whole filters in a chat (chat owner only)."""

    BUTTON_TXT = """Help: <b>Buttons</b>

- tgmoviebot support both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. IMDb supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/moviespot00100)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. Make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - connect a particular chat to your PM.
β’ /disconnect  - disconnect from a chat.
β’ /connections - list all your connections."""

    AUTO_MANUAL_TXT = """Help: <b>Filters</b>

<b>Select a filters type Below:</b>"""

    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>
β’ /paste [text] - paste the given text on Pasty
β’ /paste [reply] - paste the replied text on Pasty

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    TGRAPH_TXT = """Help: <b>TGraph & Paste</b>

Do as you wish with telegra.ph module!

<b>Commands and Usage:</b>
β’ /tgmedia or /tgraph - upload supported media (within 5MB) to telegraph.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    INFO_TXT = """Help: <b>Information</b>

Get information about something!

<b>Commands and Usage:</b>
β’ /id - get id of a specifed user.
β’ /info  - get information about a user.
β’ /json - get the json details of a message.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ These commands can be used by any group member."""

    GTRANS_TXT = """Help: <b>Google Translator</b>

Translate texts to a specific language!

<b>Commands and Usage:</b>
β’ /tr [language code][reply] - translate replied message to specific language.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on both pm and group.
β’ IMDb can translate texts to 200+ languages."""

    SEARCH_TXT = """Help: <b>IMDb</b>

Search many things without leaving telegram!

<b>Commands and Usage:</b>
β’ /imdb  - get the film information from IMDb source.
β’ /search  - get the film information from various sources.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ More search tools can be found on inline.
β’ Those commands works on both pm and group."""

    PURGE_TXT = """Help: <b>Purge</b>

Need to delete lots of messages? That's what purges are for!

<b>Commands and Usage:</b>
β’ /purge - delete all messages from the replied to message, to the current message.

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    RESTRIC_TXT = """Help: <b>Restrictions</b>

Some people need to be publicly banned; spammers, annoyances, or just trolls.

This module allows you to do that easily, by exposing some common actions, so everyone will see!

<b>Commands and Usage:</b>
β’ /ban - ban a user.
β’ /tban - temporarily ban a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /mute - mute a user.
β’ /tmute - temporarily mute a user. Example time values: 4m = 4 minutes, 3h = 3 hours, 6d = 6 days, 5w = 5 weeks.
β’ /unban or /unmute - unmute a user & unban a user.

<b>Examples:</b>
- Mute a user for two hours.
-> <code>/tmute @username 2h</code>

<b>NOTE:</b>
β’ IMDb should have admin privillage.
β’ These commands works on group.
β’ These commands can be used by Only admin."""

    ADMIN_TXT = """Help: <b>Admin Mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - to get the rescent errors.
β’ /stats - to get status of files in db.
β’ /delete - to delete a specific file from db.
β’ /users - to get list of my users and ids.
β’ /chats - to get list of the my chats and ids.
β’ /leave - to leave from a chat.
β’ /disable - do disable a chat.
β’ /ban_users - to ban a user.
β’ /unban_users - to unban a user.
β’ /channel - to get list of total connected channels.
β’ /broadcast - to broadcast a message to all users."""

    STATUS_TXT = """<b>β Total Files βΊβΊ</b> <code>{}</code>
<b>β Total Users βΊβΊ</b> <code>{}</code>
<b>β Total Chats βΊβΊ</b> <code>{}</code>
<b>β Used Storage βΊβΊ</b> <code>{}</code> MB
<b>β Free Storage βΊβΊ</b> <code>{}</code> MB"""

    FORCESUB_TXT = """**β¦οΈ READ THIS INSTRUCTION β¦οΈ**

__π£ In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately π__

**π JOIN THIS CHANNEL & TRY AGAIN π**"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

    ZOMBIES_TXT = """Help: <b>Zombies</b>

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
β’ /inkick - command with required arguments and i will kick members from group.
β’ /instatus - to check current status of chat member from group.
β’ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
β’ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
β’ /dkick - to kick deleted accounts."""

    CREATOR_REQUIRED = """βYou have to be the group creator to do that."""
      
    INPUT_REQUIRED = "β **Arguments Required**"
      
    KICKED = """βοΈ Successfully Kicked {} members according to the arguments provided."""
      
    START_KICK = """π? Removing inactive members this may take a while..."""
      
    ADMIN_REQUIRED = """βI am not an admin here\n__Leaving this chat, add me again as admin with ban user permission."""
      
    DKICK = """βοΈ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """Collecting users information..."""
      
    STATUS = """{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}
"""
