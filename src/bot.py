import os
import telebot


# Initialize bot
bot = telebot.TeleBot(
    os.environ['BOTTOKEN'], parse_mode='HTML'
)
