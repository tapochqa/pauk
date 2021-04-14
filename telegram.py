import telebot
from telebot import types
from main import *
import os

bot = telebot.TeleBot(open('token', 'r').readline())


@bot.message_handler(content_types=['text'])


def get_text_messages(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, '🕷 Напишите что-нибудь на русском')
	else:
		bot.send_message(message.from_user.id, paukize(message.text))




bot.polling(none_stop=True, interval=0)