import telebot
from secrets import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hi'])
def send_welcome(message):
	bot.reply_to(message, 'Hello, world!!')

bot.polling()
