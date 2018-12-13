from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
import os

updater = Updater(token = open("LOCALTOKEN.txt", "r").read())
dispatcher= updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Soy la lunera")

## todo: pending
def restart_and_update(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text="Actualizando...")
    print("Updating system...")

    os.system("git pull")
    os.system("pm2 restart Luna")

    bot.send_message(chat_id = update.message.chat_id, text="Actualización completa! Woof")

restart_and_update_handler = CommandHandler('update', restart_and_update)
start_handler = CommandHandler('luna', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(restart_and_update_handler)

updater.start_polling()
