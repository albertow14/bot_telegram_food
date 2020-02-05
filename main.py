import telebot
import requests
from imageio import imread

from magreator import get_info_of

from secrets import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_message = f'Hola {message.from_user.first_name} para saber el \
nutriscore de un producto, escribe su codigo de\
barras o hazle una foto'
    bot.send_message(message.chat.id, welcome_message)

# Endpoint that recieves a number and sends it to the backend to do the request to the api
@bot.message_handler(regexp='^[-+]?[0-9]+$')
def send_request_to_api(message):
    response = get_info_of(message)
    pretty_message = f'El nutriscore de _{response.get("product_name")}_ es *{response.get("nutriscore_grade","UnKnonwn").upper()}*'
    bot.send_message(message.chat.id ,pretty_message, parse_mode= 'Markdown')
    image_response = requests.get(f'{response.get("image_url")}')
    image_extension = response.get("image_url")[-3:]
    if image_response.status_code == 200:
        with open(f'{response.get("_id")}.{image_extension}', 'wb') as photo:
            photo.write(image_response.content)        
        
        with open('./temp.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)

bot.polling()
