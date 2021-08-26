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
bot_token = os.getenv('TOKEN')
chatid = os.getenv('TG_CHAT_IDS')

def send_test_sticker():
    try:
        telegram_notify = telegram.Bot(bot_token)
        telegram_notify.send_sticker(chat_id="-1001182712330", sticker='CAACAgUAAxkBAAECxHdhHK8RDiVW9UPl9nXcJzen3tgVMAACrQIAAlIJ6VRjcWIcrnhvuSAE')
    except Exception as ex:
        print(ex)

def send_test_message():
    try:
        telegram_notify = telegram.Bot(bot_token)
        message = f"""{req}*{rom}*\nFrom *{dev}*\n\n*Information:*\n`{cat}`\n*Download A/B:* [here]({dab})\n*File not found? Wait a bit, bot is uploading*\n\n*Credits:* [Erfan](https://github.com/Erfanoabdi) | [Velosh](https://t.me/Velosh) | [cyto](https://t.me/cytolytic) | [PruhMirror](https://t.me/PruhBruhNahMirror)\n*Built by @ping2109gsis\nJoin @ping2109gsischat*"""

        telegram_notify.send_message(chat_id="-1001182712330", text=message, disable_web_page_preview=True,
                                parse_mode='Markdown')
    except Exception as ex:
        print(ex)

send_test_sticker()
send_test_message()
