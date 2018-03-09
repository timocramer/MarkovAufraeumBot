#!/usr/bin/python3

# benötigt python-telegram-bot

from telegram.ext import Updater, RegexHandler
import time

TOKEN_FILE = "/etc/markov-aufraeum-bot/token.txt"

def deleteMarkovMessage(bot, update):
	time.sleep(5)
	bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)


token = open(TOKEN_FILE, "r").read().rstrip()
updater = Updater(token=token)

updater.dispatcher.add_handler(RegexHandler('/markov', deleteMarkovMessage))

updater.start_polling()
