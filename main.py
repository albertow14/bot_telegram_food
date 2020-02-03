import telebot
import requests

from magreator import get_info_of

from secrets import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Hello, world!!')

# Endpoint that recieves a number and sends it to the backend to do the request to the api
@bot.message_handler(regexp='^[-+]?[0-9]+$')
def send_request_to_api(message):
    response = get_info_of(message)
    if response.get('error'):
        bot.reply_to(message, response.get('error'))
    pretty_message = f'El nutriscore de XXXX es {response.get("nutrition_grades")}'
    bot.reply_to(message, pretty_message)




bot.polling()
