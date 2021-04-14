import telebot
from telebot import types
from main import *
import os

bot = telebot.TeleBot(open('token', 'r').readline())

def bot_log(bot, from_username, message):
	log_message = '[LOG] @{0} : {1}'.format(from_username, message)
	bot.send_message(163440129, log_message)


@bot.message_handler(content_types=['text'])


def get_text_messages(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, '🕷 Напишите что-нибудь на русском')
	else:
		reply = paukize(message.text)
		bot.send_message(message.from_user.id, reply)
		bot_log(bot, message.from_user.username, message.text)
		bot_log(bot, 'rayk_bot', reply)





bot.polling(none_stop=True, interval=0)