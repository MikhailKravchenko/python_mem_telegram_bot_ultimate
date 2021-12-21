
import telebot
import env

from telebot import types



bot = telebot.TeleBot(env.token)


def send_to_chat(message):
    if message.text == 'стоп' or message.text == 'Стоп' or message.text == 'СТОП':
        return

    x = message.photo[0].file_id
    if x is None:
        return
    chat_id = -1001210399850
    bot.send_photo(chat_id, x)


def get_photo_id(message):
    x = message.photo[0].file_id
    bot.send_message(message.chat.id, x)



def get_name(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    return mention
    # bot.send_message(cid,"Hi, " + mention + ' @' + message.from_user.username,parse_mode="Markdown")

