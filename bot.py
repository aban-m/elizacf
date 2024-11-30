import os
from configparser import ConfigParser
import telebot
from .utils import escape
from . import parsing
from . import data

__location__ = os.path.realpath(
      os.path.join(os.getcwd(), os.path.dirname(__file__)))
config = ConfigParser()
config.read(os.path.join(__location__, 'config.ini'))

TOKEN = config['bot']['token'].strip()
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
    reply('PONG', msg)

@bot.message_handler(commands=['pick'])
def com_pick(msg):
    text = msg.text.split(' ', maxsplit=1)+['']

    try:
        cond = parsing.parse_conditions(text[1])
        print(cond)
    except Exception as e:
        print(e)
        reply('Parsing failed.', msg)
        return

    result = data.find(cond, count = 1)
    if not result:
        reply('**No matches.**', msg)
        return

    reply(data.represent_problem(result[0]), msg)
