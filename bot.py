import telebot
from utils import escape

bot = telebot.TeleBot(TOKEN, parse_mode='MarkdownV2',
                      threaded = True
                      )

# some utility functions
def reply(text, msg, fr=True):
    if not fr:
        bot.send_message(msg.chat.id, escape(text))
    else:
        bot.reply_to(msg, escape(text))


@bot.message_handler(commands=['ping'])
def com_ping(msg):
    bot.send_message(msg.chat.id, 'PONG')

