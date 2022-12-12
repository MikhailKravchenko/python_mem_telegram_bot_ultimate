# -*- coding: utf-8 -*-

import telebot

import config
import env

from telebot import types

from SQLighter import SQLighter

bot = telebot.TeleBot(env.token)


def send_to_chat(message):
    if message.text == 'стоп' or message.text == 'Стоп' or message.text == 'СТОП':
        return
    x = message.photo[0].file_id
    if x is None:
        return
    chat_id = -1001210399850
    bot.send_photo(chat_id, x, caption=message.caption)

def get_photo_id(message):
    x = message.photo[0].file_id
    bot.send_message(message.chat.id, x)

def get_name(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = "[" + user_name + "](tg://user?id=" + str(user_id) + ")"
    return mention
    # bot.send_message(cid,"Hi, " + mention + ' @' + message.from_user.username,parse_mode="Markdown")

def custom_key(people):
    return people[0]


async def services_next_content_control(self, message: telebot.types.Message) -> None:
    """
    """
    db_worker = SQLighter(config.database_name)
    is_admin_chat = db_worker.get_admin_chat(message)
    if is_admin_chat:
        chat_id = is_admin_chat[0][1]
        x = db_worker.select_file_id_for_content_control(chat_id)
        if x == None: return
        photo_id = x[0][0]

        markup = types.InlineKeyboardMarkup(row_width=2)
        bt1 = types.InlineKeyboardButton('Delete', callback_data='content_control_delete_' + str('photo_id'))
        bt2 = types.InlineKeyboardButton('Next', callback_data='content_control_next' + str('ratio_id'))
        markup.add(bt1, bt2)
        try:
            await self.bot.send_photo(message.chat.id,
                                        photo=photo_id,
                                        reply_markup=markup)
        except Exception as e:

            await self.bot.send_message(message.chat.id, e)