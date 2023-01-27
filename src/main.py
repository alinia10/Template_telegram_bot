import os

import telebot
from loguru import logger
from src.utils.io import write_json


class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['BOTTOKEN'])
		self.echo_all = self.bot.message_handler(
			func=lambda message: True)(
				self.echo_all)


	def run(self):
		logger.info('Bot Is Runnin...')
		self.bot.infinity_polling()
	def echo_all(self, message):
		write_json(message.json,'messge.json')
		self.bot.reply_to(message, message.text)

if __name__ == '__main__':
	logger.info('Bot strated.')
	bot = Bot()
	bot.run()
	logger.info('Done!.')

