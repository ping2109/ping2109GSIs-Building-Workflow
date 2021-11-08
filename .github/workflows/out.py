import os
import telegram
from telegram import Sticker, PhotoSize, TelegramError, StickerSet, MaskPosition, Bot
from telegram.error import BadRequest

with open('ping2109.txt') as f:
    os.environ['CAT_FILE'] = f.read()

rom = os.getenv('POST_TITLE')
dev = os.getenv('DEVICE')
cat = os.getenv('CAT_FILE')
req = os.getenv('REQUEST')
dab = os.getenv('SOURCEFORGE')
dab2 = os.getenv('SOURCEFORGE2')
bot_token = os.getenv('TOKEN')
channel = os.getenv('CHAT_ID')
chatid = os.getenv('TG_CHAT_IDS')
notice = os.getenv('NOTICE')

def send_test_sticker():
    try:
        telegram_notify = telegram.Bot(bot_token)
        telegram_notify.send_sticker(chat_id=channel, sticker='CAACAgUAAxkBAAEDPGlhh9FuLPh1arHg7QZ-pyOJW6eI_wACEwQAAljWQFQcf8h6zv-jTyIE')
    except Exception as ex:
        print(ex)

def send_test_message():
    try:
        telegram_notify = telegram.Bot(bot_token)
        message = f"""{req}*{rom}*\nFrom *{dev}*\n\n*Information:*\n`{cat}`\n*Builder's notes:*\n{notice}\n\n*Download A/B:* [here]({dab})\n*Download A only:* [here]({dab2})\n*File not found? Wait a bit, SF server is mirroring*\n\n*Credits:* [Erfan](https://github.com/Erfanoabdi) | [Velosh](https://t.me/Velosh) | [cyto](https://t.me/cytolytic) | [PruhMirror](https://t.me/PruhBruhNahMirror)\n*Built by @ping2109gsis\nJoin @ping2109gsischat*"""

        telegram_notify.send_message(chat_id=channel, text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
    except Exception as ex:
        print(ex)

send_test_sticker()
send_test_message()
