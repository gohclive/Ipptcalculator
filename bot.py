import os
from dotenv import load_dotenv
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import Update
import logging


load_dotenv()
api_key = os.getenv("API_KEY")
updater = Updater(token = api_key, use_context= True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


