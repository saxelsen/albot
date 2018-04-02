import telebot
from reply_handler import get_reply
from secret_settings import BOT_API_TOKEN

bot = telebot.TeleBot(token=BOT_API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, I am Albot. People consider me an oracle, so feel free to ask any questions you might have!")


@bot.message_handler(regexp=r'.+')
def reply_to_message(message):
    reply = get_reply(message)
    bot.reply_to(message, reply)


if __name__ == '__main__':
    bot.polling()
