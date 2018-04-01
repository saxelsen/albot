import telebot
from secret_settings import BOT_API_TOKEN

bot = telebot.TeleBot(token=BOT_API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hi, I am Albot. What can I do you for?')


if __name__ == '__main__':
    bot.polling()
