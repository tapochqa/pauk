import telebot
from telebot import types
from main import *

bot = telebot.TeleBot('303673800:AAF4Ej2f1zp9c5lepXo-9JWganA-6v7eGnM')


@bot.message_handler(content_types=['text'])


def get_text_messages(message):
	if message.text == "/start":
		bot.send_message(message.from_user.id, '🕷 Напишите что-нибудь на русском')
	else:
		bot.send_message(message.from_user.id, paukize(message.text))

bot.polling(none_stop=True, interval=0)