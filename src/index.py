from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging

updater = Updater(token = open("LOCALTOKEN.txt", "r").read())
dispatcher= updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Soy la lunera")

start_handler = CommandHandler('Luna', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
