"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "വെറുതെ Alive അടിച്ചു വെറുപ്പിക്കാതട ഞൻ ഇവട ജീവനോടെ ഒക്കെ തന്നെയുണ്ട് ചത്തൊന്നും പോയിട്ടില്ല 🥲"
HELP = "Help ഒന്നും ഇല്ല ഓടിക്കോ...."
REPO = "https://github.com/Zinan100/REXER"
HI   = "HELLO പോയിട്ട് /START അടിയടോ ഇല്ലാതെ ഹി പറയാൻ മനീഷ്യൻ അല്ലാ ബോട്ടാ"
SERVICES = "Hey, Buddy..😊

Our Services..⚡️

✮ File Store Bot ✅ ›› ₹90
✮ Url Uplaoder Bot ✅ ›› ₹90
✮ File Rename Bot ✅ ›› ₹90
✮ Button Poster Creator Bot ›› ✅ ₹80
✮ Movie Search Bot Inline / Group  ✅ ›› ₹125
(If You Want To Avoid Your Public Group From Copyright Use This Bot) 

Auto Filter Bot ✅

✮ IMDB Version 3 Bot 🦋 ›› ₹150

With IMDB | Force Channel/Group Join | Single And Double Button  | Custom IMDB Template | Multiple Group Connection | Start Message With Pic | Can Remove File Individually From Database....

✮ IMDB Version 3 Bot 🦋 ›› ₹200
(With Extra Features)

With IMDB | Force Channel/Group Join | Single And Double Button  | Custom IMDB Template | Multiple Group Connection | Start Message With Pic | Can Remove File Individually From Database | Google Translate | User Information | Ban & Mute | Inline Movie Search | Photo/Video To Telegram Link | Fun Entertainment | Song Download From YouTube | Video Download From YouTube | COVID Information | Sticker ID...

Contact ›› @PaidServiceMW_Bot"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", COMMAND_HAND_LER) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
