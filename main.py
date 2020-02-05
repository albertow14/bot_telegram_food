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
    pretty_message = f'El nutriscore de _{response.get("product_name")}_ es *{response.get("nutriscore_grade","UnKnonwn").upper()}*'
    bot.reply_to(message, pretty_message, parse_mode= 'Markdown')




bot.polling()
