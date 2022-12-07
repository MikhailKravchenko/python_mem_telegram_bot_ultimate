# -*- coding: utf-8 -*-
import asyncio
import json
import logging
import os
import random
import re
import sqlite3
import ssl
import urllib
from datetime import datetime

import requests
import telebot
from aiohttp import web
from telebot import types
from telebot.async_telebot import AsyncTeleBot

import hash_image
import servises
from wednesday import IMAGES
import config
import utils
from abstract import AbstractCore
from decor import exception, info_log_message_async, info_log_message_async_callback
from env import (
    WEBHOOK_LISTEN,
    WEBHOOK_PORT,
    WEBHOOK_SSL_CERT,
    WEBHOOK_SSL_PRIV,
    WEBHOOK_URL_BASE,
    WEBHOOK_URL_PATH,
    token,
    webhook, WEBHOOK_HOST,
)
from SQLighter import SQLighter

app = web.Application()


class Core(AbstractCore):
    """ Bot core. Starts listening for new messages.
         Responsible for calling methods on certain commands from the chat and for pressing buttons
        """

    def __init__(self) -> None:
        self.bot = AsyncTeleBot(token)

        @self.bot.message_handler(commands=['start'])
        @exception
        async def _command_start(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /start"""
            await self.process_comand_start(message)

        @self.bot.message_handler(commands=['black_list'])
        @exception
        async def _command_black_list(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /black_list"""
            await self.process_comand_black_list(message)

        @self.bot.message_handler(commands=['admin'])
        @exception
        async def _command_admin(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /admin"""

            await self.process_comand_admin(message)

        @self.bot.message_handler(commands=['setadminchat'])
        @exception
        async def _command_set_admin_chat(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /setadminchat"""

            await self.process_set_admin_chat(message)

        @self.bot.message_handler(commands=['mem'])
        @exception
        async def _command_mem(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /statistic"""

            await self.process_get_mem(message)

        @self.bot.message_handler(commands=['wednesday'])
        @exception
        async def _command_wednesday(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /wednesday"""
            await self.process_command_wednesday(message)

        @self.bot.message_handler(commands=['happy1'])
        @exception
        async def _command_happy1(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /happy1"""
            await self.process_command_happy1(message)

        @self.bot.message_handler(commands=['happy2'])
        @exception
        async def _command_happy2(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /happy2"""
            await self.process_command_happy2(message)

        @self.bot.message_handler(commands=['happy3'])
        @exception
        async def _command_happy3(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /happy3"""
            await self.process_command_happy3(message)

        @self.bot.message_handler(commands=['gud'])
        @exception
        async def _command_gud(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /gud"""
            await self.process_command_gud(message)

        @self.bot.message_handler(commands=['cash'])
        @exception
        async def _command_cash(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /cash"""
            await self.process_command_cash(message)

        @self.bot.message_handler(commands=['top'])
        @exception
        async def _command_top(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /top"""
            await self.process_command_top(message)

        @self.bot.message_handler(commands=['top7'])
        @exception
        async def _command_top7(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /top7"""
            await self.process_command_top7(message)

        @self.bot.message_handler(commands=['top30'])
        @exception
        async def _command_top30(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /top30"""
            await self.process_command_top30(message)

        @self.bot.message_handler(commands=['tophunya'])
        @exception
        async def _command_tophunya(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /tophunya"""
            await self.process_command_tophunya(message)

        @self.bot.message_handler(commands=['tophunya7'])
        @exception
        async def _command_tophunya7(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /tophunya7"""
            await self.process_command_tophunya7(message)

        @self.bot.message_handler(commands=['tophunya30'])
        @exception
        async def _command_tophunya30(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /tophunya30"""
            await self.process_command_tophunya30(message)

        @self.bot.message_handler(commands=['antitophunya'])
        @exception
        async def _command_antitophunya(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /antitophunya"""
            await self.process_command_antitophunya(message)

        @self.bot.message_handler(commands=['toplionhunya'])
        @exception
        async def _command_toplionhunya(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /toplionhunya"""
            await self.process_command_toplionhunya(message)

        @self.bot.message_handler(commands=['helper'])
        @exception
        async def _command_helper(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /helper"""
            await self.process_command_helper(message)

        @self.bot.message_handler(commands=['debt'])
        @exception
        async def _command_debt(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /debt"""
            await self.process_command_debt(message)

        @self.bot.message_handler(commands=['message'])
        @exception
        async def _command_message(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /message"""
            await self.process_command_message(message)

        @self.bot.message_handler(commands=['f'])
        @exception
        async def _command_f(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a command is entered /f"""
            await self.process_command_f(message)

        @self.bot.message_handler(content_types=["new_chat_members"])
        @exception
        async def _content_new_chat_members(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a content is entered new_chat_members"""
            await self.process_content_new_chat_members(message)

        @self.bot.message_handler(content_types=["photo"])
        @exception
        async def _content_photo(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a content is entered photo"""
            await self.process_content_photo(message)

        @self.bot.message_handler(content_types=["video"])
        @exception
        async def _content_video(message: telebot.types.Message or telebot.types.CallbackQuery) -> None:
            """Fires when a content is entered video"""
            await self.process_content_video(message)

        @self.bot.message_handler(func=lambda message: True, content_types=['text'])
        @exception
        async def _get_text_messages(message: telebot.types.Message) -> None:
            """Fires when any text message is received"""
            await self.process_get_text_messages(message)

        @self.bot.callback_query_handler(func=lambda c: True)
        @exception
        @info_log_message_async_callback
        async def process_callback_btn(c: types.CallbackQuery) -> None:
            """Fires when the Details button is clicked.
            """
            db_worker = SQLighter(config.database_name)

            try:
                db_worker.save_id_chat_callback(c)
            except sqlite3.IntegrityError:
                None
            db_worker.close()
            data = c.data
            clear_data = re.sub(r'[^\w\s]+|[\d]+', r'', data).strip()
            if clear_data == 'Like_':

                callback_ratio_id = (int(''.join(filter(str.isdigit, data))))

                user_id = c.from_user.username
                if user_id is None:
                    user_id = c.from_user.id

                db_worker = SQLighter(config.database_name)
                like = db_worker.select_ratio_to_like_to_user(callback_ratio_id, user_id)

                if like:
                    db_worker.update_ratio_like_off(callback_ratio_id)
                    db_worker.update_ratio_to_like_off(callback_ratio_id, user_id)
                    ratio_value = db_worker.select_ratio_value(callback_ratio_id)
                    ratio_dislike_value = db_worker.select_ratio_dislike_value(callback_ratio_id)
                    db_worker.close()

                    ratio_value = u'\U0001F49A' + ' ' + str(ratio_value)
                    ratio_dislike_value = u'\U0001F621' + ' ' + str(ratio_dislike_value)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    bt1 = types.InlineKeyboardButton(ratio_value, callback_data='Like_' + str(callback_ratio_id))
                    bt2 = types.InlineKeyboardButton(ratio_dislike_value,
                                                     callback_data='Dislike_' + str(callback_ratio_id))

                    markup.add(bt1, bt2)
                    await self.bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id,
                                                             reply_markup=markup)
                    await self.bot.answer_callback_query(c.id, text='Ваш голос убран')

                else:

                    db_worker.update_ratio_like(callback_ratio_id)
                    db_worker.update_ratio_to_like(callback_ratio_id, user_id)
                    ratio_value = db_worker.select_ratio_value(callback_ratio_id)
                    ratio_dislike_value = db_worker.select_ratio_dislike_value(callback_ratio_id)
                    db_worker.close()

                    ratio_value = u'\U0001F49A' + ' ' + str(ratio_value)
                    ratio_dislike_value = u'\U0001F621' + ' ' + str(ratio_dislike_value)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    bt1 = types.InlineKeyboardButton(ratio_value, callback_data='Like_' + str(callback_ratio_id))
                    bt2 = types.InlineKeyboardButton(ratio_dislike_value,
                                                     callback_data='Dislike_' + str(callback_ratio_id))

                    markup.add(bt1, bt2)
                    await self.bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id,
                                                             reply_markup=markup)
                    await self.bot.answer_callback_query(c.id, text='Ваш голос учтен')

                    # bot.answer_callback_query(c.message.chat.id, 'Конфиг пуст', reply_markup=markup)
            if clear_data == 'Dislike_':

                callback_ratio_id = (int(''.join(filter(str.isdigit, data))))

                user_id = c.from_user.username
                if user_id is None:
                    user_id = c.from_user.id

                db_worker = SQLighter(config.database_name)
                like = db_worker.select_ratio_to_dislike_to_user(callback_ratio_id, user_id)

                if like == True:

                    db_worker.update_ratio_dislike_off(callback_ratio_id)
                    db_worker.update_ratio_to_dislike_off(callback_ratio_id, user_id)
                    ratio_value = db_worker.select_ratio_value(callback_ratio_id)
                    ratio_dislike_value = db_worker.select_ratio_dislike_value(callback_ratio_id)
                    db_worker.close()

                    ratio_value = u'\U0001F49A' + ' ' + str(ratio_value)
                    ratio_dislike_value = u'\U0001F621' + ' ' + str(ratio_dislike_value)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    bt1 = types.InlineKeyboardButton(ratio_value, callback_data='Like_' + str(callback_ratio_id))
                    bt2 = types.InlineKeyboardButton(ratio_dislike_value,
                                                     callback_data='Dislike_' + str(callback_ratio_id))

                    markup.add(bt1, bt2)
                    await self.bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id,
                                                             reply_markup=markup)

                    await self.bot.answer_callback_query(c.id, text='Ваш голос убран')
                else:

                    db_worker.update_ratio_dislike(callback_ratio_id)
                    db_worker.update_ratio_to_dislike(callback_ratio_id, user_id)
                    ratio_value = db_worker.select_ratio_value(callback_ratio_id)
                    ratio_dislike_value = db_worker.select_ratio_dislike_value(callback_ratio_id)
                    db_worker.close()

                    ratio_value = u'\U0001F49A' + ' ' + str(ratio_value)
                    ratio_dislike_value = u'\U0001F621' + ' ' + str(ratio_dislike_value)
                    markup = types.InlineKeyboardMarkup(row_width=1)
                    bt1 = types.InlineKeyboardButton(ratio_value, callback_data='Like_' + str(callback_ratio_id))
                    bt2 = types.InlineKeyboardButton(ratio_dislike_value,
                                                     callback_data='Dislike_' + str(callback_ratio_id))

                    markup.add(bt1, bt2)
                    await self.bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id,
                                                             reply_markup=markup)
                    await self.bot.answer_callback_query(c.id, text='Ваш голос учтен')

                    # bot.answer_callback_query(c.message.chat.id, 'Конфиг пуст', reply_markup=markup)
            if data == 'get_groshi':
                await self.bot.answer_callback_query(c.id, text='Грошi высланы на счет')

    @info_log_message_async
    @exception
    async def process_comand_start(self, message: telebot.types.Message) -> None:
        """/start command method
             Sends a welcome message
            """
        await self.bot.send_message(message.chat.id,
                                    '👋🏻 Hello. I am a Memebot. I am made for meme chats,'
                                    ' I keep track of all memes and compare with those that have already been sent.'
                                    ' If there is a repeat, I will let you know. For each meme (photo and video), '
                                    'I send voting buttons. In the admin chat you can see the top for the week, '
                                    'month and year. And display messages in the main chat.')

    @info_log_message_async
    @exception
    async def process_comand_black_list(self, message: telebot.types.Message) -> None:
        """/black_list
            """
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id_meme_chat = is_admin_chat[0][1]
        text = message.text[11:].replace("@", "").replace(" ", "")
        db_worker.set_user_in_black_list(chat_id_meme_chat, text)

    @info_log_message_async
    @exception
    async def process_comand_admin(self, message: telebot.types.Message) -> None:
        """

        :param message: telebot.types.Message
        :return:
        /admin command method
         If there is no admin chat, then he proposes to assign
         If there is and the command is sent in the admin chat, then it gives help on the admin commands
         If there is and the chat is not Alminsky, it simply ignores


        """
        db_worker = PostgreSQL()
        admin_chat_id = db_worker.get_admin_chat_id()
        if not admin_chat_id:
            await self.bot.send_message(message.chat.id, "There is no admin chat yet.\n"
                                                         "To make this chat the bot admin's chat,"
                                                         " enter command /setadminchat")
            return
        if admin_chat_id[0][0] == message.chat.id:
            await self.bot.send_message(message.chat.id,
                                        '/statistic - Get bot statistics \n'
                                        )

    @info_log_message_async
    @exception
    async def process_set_admin_chat(self, message: telebot.types.Message) -> None:
        """
        Designates the current chat as the admin chat if it is not assigned
        """
        db_worker = SQLighter(config.database_name)

        if db_worker.set_admin_chat_in_db(message):

            await self.bot.send_message(message.chat.id,
                                        'Now this chat is admin, all admin commands are available \n'
                                        )
        else:
            await self.bot.send_message(message.chat.id,
                                        'This bot already has an admin chat assigned')

    @info_log_message_async
    @exception
    async def process_get_mem(self, message: telebot.types.Message) -> None:
        """
        """
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            message.chat.id == is_admin_chat[0][2]
            chat_id = is_admin_chat[0][1]
            x = utils.get_id_photo_for_chat(chat_id)
            if x == None: return
            # Выбираем случайный элемент списка
            photo_id = x[random.randrange(0, len(x), 1)]
            # Отсылаем в чат
            await self.bot.send_photo(chat_id, photo=photo_id)
        else:
            x = utils.get_id_photo_for_chat(message.chat.id)

            if x == None: return
            # Выбираем случайный элемент списка
            photo_id = x[random.randrange(0, len(x), 1)]
            # Отсылаем в чат
            await self.bot.send_photo(message.chat.id, photo=photo_id)

    @info_log_message_async
    @exception
    async def process_command_wednesday(self, message: telebot.types.Message) -> None:
        """
        """
        now = datetime.now()
        day_now = datetime.isoweekday(now)
        if day_now == 3:
            URL = IMAGES[day_now.__str__()][random.randint(0, len(IMAGES[day_now.__str__()]) - 1)]
            response = requests.get(URL)
            src = os.getcwd() + '\\image\\' + str(message.date) + '.jpeg'
            open(src, "wb").write(response.content)
            immagesss = open(src, 'rb')
            await self.bot.send_photo(message.chat.id, immagesss)
            del immagesss
            if os.path.isfile(src):
                os.remove(src)
        else:
            list_day = [str(day_now), 'any', 'notWednesday']
            random_choice = random.choice(list_day)
            URL = IMAGES[random_choice][random.randint(0, len(IMAGES[random_choice]) - 1)]

            response = requests.get(URL)
            src = os.getcwd() + '\\image\\' + str(message.date) + '.jpeg'
            open(src, "wb").write(response.content)
            immagesss = open(src, 'rb')
            await self.bot.send_photo(message.chat.id, immagesss)
            del immagesss
            if os.path.isfile(src):
                os.remove(src)

    @info_log_message_async
    @exception
    async def process_command_happy1(self, message: telebot.types.Message) -> None:
        """
        """
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
            await self.bot.send_message(chat_id,
                                        f"Зарплатонька пришла! <3")
            video_id = 'BAACAgIAAxkBAAIEcmDZoRe-LA3QzjetEJdOTezCAAGu5wACpgoAAmt1WEo3ZqrbnJ8IkyAE'
            await self.bot.send_video(chat_id, video_id)
        else:

            await self.bot.send_message(message.chat.id,
                                        f"Зарплатонька пришла!")
            video_id = 'BAACAgIAAxkBAAIEcmDZoRe-LA3QzjetEJdOTezCAAGu5wACpgoAAmt1WEo3ZqrbnJ8IkyAE'
            await self.bot.send_video(message.chat.id, video_id)

    @info_log_message_async
    @exception
    async def process_command_happy2(self, message: telebot.types.Message) -> None:
        """
        """
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]

            await self.bot.send_message(chat_id,
                                        f"Зарплатонька пришла! <3")
            video_id = 'BAACAgIAAxkBAAIi5GIDtRHNy4EMZvOoq712hREwZ66kAAITEgAC6feYSDxMbJ2_DrFOIwQ'
            await self.bot.send_video(chat_id, video_id)
        else:

            await self.bot.send_message(message.chat.id,
                                        f"Зарплатонька пришла!")
            video_id = 'BAACAgIAAxkBAAIi5GIDtRHNy4EMZvOoq712hREwZ66kAAITEgAC6feYSDxMbJ2_DrFOIwQ'
            await self.bot.send_video(message.chat.id, video_id)

    @info_log_message_async
    @exception
    async def process_command_happy3(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]

            await self.bot.send_message(chat_id,
                                        f"Зарплатонька пришла! <3")
            video_id = 'BAACAgIAAxkBAAIlFmJTTJgx0ZO7Tvp3KRVYLJuyNT4dAAIDGgACs1OYSlyrbCsG6j6EIwQ'
            await self.bot.send_video(chat_id, video_id)
        else:

            await self.bot.send_message(message.chat.id,
                                        f"Зарплатонька пришла!")
            video_id = 'BAACAgIAAxkBAAIlFmJTTJgx0ZO7Tvp3KRVYLJuyNT4dAAIDGgACs1OYSlyrbCsG6j6EIwQ'
            await self.bot.send_video(message.chat.id, video_id)

    @info_log_message_async
    @exception
    async def process_command_gud(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
            # AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E

            photo_id = 'AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E'

            await self.bot.send_photo(chat_id, photo=photo_id)

    @info_log_message_async
    @exception
    async def process_command_cash(self, message: telebot.types.Message) -> None:

        # Создаем кнопки и записываем их в переменную
        start_markup = telebot.types.InlineKeyboardMarkup()

        # первый ряд (две кнопки)
        btn0 = telebot.types.InlineKeyboardButton('Дайте грошi', callback_data='get_groshi')
        start_markup.row(btn0)
        await self.bot.send_message(message.chat.id, 'Шо надо?',
                                    reply_markup=start_markup)

    @info_log_message_async
    @exception
    async def process_command_top(self, message: telebot.types.Message) -> None:

        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
            top = db_worker.ratio_rating_all_time_for_top(chat_id)
            db_worker.close()

            ratio = top[1]
            photo_id = top[2]
            username = top[3]
            message_id = top[5]
            data_id = top[7]

            if int(data_id) == 0:
                await self.bot.send_photo(chat_id, photo=photo_id)
                try:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время',
                                                reply_to_message_id=message_id)
                except:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время')
            elif int(data_id) == 1:
                await self.bot.send_video(chat_id, data=photo_id)
                try:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время',
                                                reply_to_message_id=message_id)
                except:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время')

        else:
            chat_id = message.chat.id
            db_worker = SQLighter(config.database_name)
            top = db_worker.ratio_rating_7days(chat_id)
            db_worker.close()
            try:
                ratio = top[1]
                photo_id = top[2]
                username = top[3]
                message_id = top[5]
                data_id = top[7]
                if int(data_id) == 0:
                    await self.bot.send_photo(message.chat.id, photo=photo_id)
                    try:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
                elif int(data_id) == 1:
                    await self.bot.send_video(message.chat.id, data=photo_id)
                    try:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
            except IndexError:
                await self.bot.send_message(message.chat.id,
                                            f'Нет ни одного мема в базе')

    @info_log_message_async
    @exception
    async def process_command_top7(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
            db_worker = SQLighter(config.database_name)
            top = db_worker.ratio_rating_7days(chat_id)
            db_worker.close()

            ratio = top[1]
            photo_id = top[2]
            username = top[3]
            message_id = top[5]
            data_id = top[7]

            if int(data_id) == 0:
                await self.bot.send_photo(chat_id, photo=photo_id)
                try:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                reply_to_message_id=message_id)
                except:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
            elif int(data_id) == 1:
                await self.bot.send_video(chat_id, data=photo_id)
                try:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                reply_to_message_id=message_id)
                except:
                    await self.bot.send_message(chat_id,
                                                f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')

        else:
            chat_id = message.chat.id
            db_worker = SQLighter(config.database_name)
            top = db_worker.ratio_rating_7days(chat_id)
            db_worker.close()
            try:
                ratio = top[1]
                photo_id = top[2]
                username = top[3]
                message_id = top[5]
                data_id = top[7]
                if int(data_id) == 0:
                    await self.bot.send_photo(message.chat.id, photo=photo_id)
                    try:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
                elif int(data_id) == 1:
                    await self.bot.send_video(message.chat.id, data=photo_id)
                    try:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
            except IndexError:
                await self.bot.send_message(message.chat.id,
                                            f'Нет ни одного мема в базе')

    @info_log_message_async
    @exception
    async def process_command_top30(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
            db_worker = SQLighter(config.database_name)
            top = db_worker.ratio_rating_30days(chat_id)
            db_worker.close()
            try:
                ratio = top[1]
                photo_id = top[2]
                username = top[3]
                message_id = top[5]
                data_id = top[7]

                if int(data_id) == 0:
                    await self.bot.send_photo(chat_id, photo=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
                elif int(data_id) == 1:
                    await self.bot.send_video(chat_id, data=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
            except IndexError:
                await self.bot.send_message(message.chat.id,
                                            f'Нет ни одного мема в базе')

        else:
            chat_id = message.chat.id
            db_worker = SQLighter(config.database_name)
            top = db_worker.ratio_rating_30days(chat_id)
            db_worker.close()
            try:

                ratio = top[1]
                photo_id = top[2]
                username = top[3]
                message_id = top[5]
                data_id = top[7]

                if int(data_id) == 0:
                    await self.bot.send_photo(message.chat.id, photo=photo_id)
                    try:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
                elif int(data_id) == 1:
                    await self.bot.send_video(message.chat.id, data=photo_id)
                    try:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(message.chat.id,
                                                    f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
            except IndexError:
                await self.bot.send_message(message.chat.id,
                                            f'Нет ни одного мема в базе')

    async def process_command_tophunya(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            mem_chat = is_admin_chat[0][1]
            chat_id = message.chat.id
            top = db_worker.ratio_rating_all_time(mem_chat)
            i = 0

            for el in top:

                ratio = top[i][1]
                photo_id = top[i][2]
                username = top[i][3]
                message_id = top[i][5]
                data_id = top[i][7]
                i = i + 1
                if int(data_id) == 0:
                    await self.bot.send_photo(chat_id, photo=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username} ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')
                elif int(data_id) == 1:
                    await self.bot.send_video(chat_id, data=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')

    @info_log_message_async
    @exception
    async def process_command_tophunya7(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            mem_chat = is_admin_chat[0][1]
            chat_id = message.chat.id
            top = db_worker.ratio_rating_3_7days(mem_chat)
            db_worker.close()
            i = 0

            for el in top:

                ratio = top[i][1]
                photo_id = top[i][2]
                username = top[i][3]
                message_id = top[i][5]
                data_id = top[i][7]
                i = i + 1
                if int(data_id) == 0:
                    await self.bot.send_photo(chat_id, photo=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username} ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')
                elif int(data_id) == 1:
                    await self.bot.send_video(chat_id, data=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')

    @info_log_message_async
    @exception
    async def process_command_tophunya30(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            mem_chat = is_admin_chat[0][1]
            chat_id = message.chat.id
            top = db_worker.ratio_rating_3_7days(mem_chat)
            db_worker.close()
            i = 0

            for el in top:

                ratio = top[i][1]
                photo_id = top[i][2]
                username = top[i][3]
                message_id = top[i][5]
                data_id = top[i][7]
                i = i + 1
                if int(data_id) == 0:
                    await self.bot.send_photo(chat_id, photo=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username} ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце')
                elif int(data_id) == 1:
                    await self.bot.send_video(chat_id, data=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце')

    @info_log_message_async
    @exception
    async def process_command_antitophunya(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            mem_chat = is_admin_chat[0][1]
            chat_id = message.chat.id
            top = db_worker.anti_ratio_rating_all_time(mem_chat)
            db_worker.close()
            i = 0

            for el in top:

                ratio = top[i][6]
                photo_id = top[i][2]
                username = top[i][3]
                message_id = top[i][5]
                data_id = top[i][7]
                i = i + 1
                if int(data_id) == 0:
                    await self.bot.send_photo(chat_id, photo=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username} ' + str(
                                                        i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!')
                elif int(data_id) == 1:
                    await self.bot.send_video(chat_id, data=photo_id)
                    try:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!',
                                                    reply_to_message_id=message_id)
                    except:
                        await self.bot.send_message(chat_id,
                                                    f' @{username}  ' + str(
                                                        i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!')

    @info_log_message_async
    @exception
    async def process_command_toplionhunya(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
        users = db_worker.top_lion_get_users(message)
        top_lion_list = []
        for user in users:
            mem_ratio = db_worker.top_lion_ratio(user)
            # print(user , ' - ',len(mem_ratio), '\n')
            pretop_lion_list = [len(mem_ratio), '@' + str(user + f' \n')]
            top_lion_list.append(pretop_lion_list)
        db_worker.close()

        top_lion_list.sort(reverse=True, key=servises.custom_key)

        top_lion_str = ''

        for top_lion in top_lion_list:
            if top_lion[0] == 0: break

            top_lion_str = top_lion_str + str(top_lion[0]) + ' - ' + str(top_lion[1])

        await self.bot.send_message(chat_id, top_lion_str)

    @info_log_message_async
    @exception
    async def process_command_helper(self, message: telebot.types.Message) -> None:
        text = f'/mem Отправить мем  \n' \
               f' \n' \
               f'/happy1 Пришла зартплата мульт  \n' \
               f' \n' \
               f'/happy2 Пришла зарплата мышь \n' \
               f'  \n' \
               f'/gud  это шедевр \n' \
               f'  \n' \
               f'/top топ за все время в чат(не проверял как работает) \n' \
               f'  \n' \
               f'/top7 топ 7 в чат \n' \
               f' \n' \
               f'/top30 топ 30 в чат\n' \
               f' \n' \
               f'/tophunya посмотреть топ за все время \n' \
               f' \n' \
               f'/tophunya7 посмотреть топ 7\n' \
               f' \n' \
               f'/tophunya30 посмотреть топ 30\n' \
               f'' \
               f'\n' \
               f'/antitophunya посмотреть топы дизлайков\n' \
               f'\n' \
               f'load_photo_in_db узнать photo_id\n' \
               f'\n' \
               f'send_to_chat прикрепить этот текст к изображению и отправить фото в чат мемов (пишем желаемый текст после  текст)\n' \
               f'\n' \
               f'/toplionhunya - все самолайки' \
               f'\n' \
               f'/debt долги по мемам' \
               f'\n' \
            # \
        await self.bot.send_message(message.chat.id, text)

    @info_log_message_async
    @exception
    async def process_command_debt(self, message: telebot.types.Message) -> telebot.types.Message:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][2]
            message.chat.id = is_admin_chat[0][1]
        db_worker = SQLighter(config.database_name)
        users = db_worker.get_users_from_chat(message)
        debt_users = []
        for user in users:
            ou = db_worker.check_mem_chat(message, user)
            if ou is False:
                debt_users.append(user)
        db_worker.close()

        if bool(debt_users) is False: return await self.bot.send_message(chat_id, 'Долгов нет')
        debt_users_str = ''

        for debt in debt_users:
            debt_users_str = debt_users_str + '@ ' + str(debt) + f' \n'

        await self.bot.send_message(chat_id, debt_users_str)

    @info_log_message_async
    @exception
    async def process_command_message(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)
        is_admin_chat = db_worker.get_admin_chat(message)
        if is_admin_chat:
            chat_id = is_admin_chat[0][1]
            text = message.text[9:]
            await self.bot.send_message(message.chat.id, text)

    @info_log_message_async
    @exception
    async def process_command_f(self, message: telebot.types.Message) -> None:
        list_photo_id = [
            'AgACAgIAAxkBAAIbeWG_wG91XsfV-dGUxCy6_RHFAAE9gAACW7QxG2waAUpXMmLDR2MLpAEAAwIAA3MAAyME',
            'AgACAgIAAxkBAAIbfWG_wLmbcDKUSkGMdfqD5ju_bB6cAAJctDEbbBoBSkhMPdxI-rnBAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbgWG_wNAUjoUg4ORLRvrOCVe0RIu6AAJdtDEbbBoBSrr9zpyEdA9rAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbhWG_wOP1rcik7qpW_0Hy-IWCwmRLAAJetDEbbBoBSliW8YSFD9BgAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbiWG_wS5WqHinAl9UKAdP5RIlLLWBAAJftDEbbBoBSv4Bgq52QKUAAQEAAwIAA3MAAyME',
            'AgACAgIAAxkBAAIbjWG_wXa5Rz8-qsDp3b7lhz41XrzaAAJgtDEbbBoBSgbKSIt05hCUAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbkWG_wZ7d5rg29m5T3rCgTAW6PMhLAAJhtDEbbBoBShZDcd3ieRBvAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIblWG_wbpuqMTTPoUs47lw_aLqAo2nAAJitDEbbBoBShpObOBI_NzFAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbmWG_weEeHm-GVSCiiI_wnx7BN1mwAAJjtDEbbBoBSif7nJNvm59WAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbnWG_wfpNCCv7vKNzIbgWoTVtrrYQAAJktDEbbBoBSkttRgkyXNbxAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIboWG_whGd2rvNDVXzo5q_8Zf5nfHlAAJltDEbbBoBSu2mrJbHZlULAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbpWG_wj4KLNEObF5Q636nZXEdyY5VAAJmtDEbbBoBSoft60dQ5Q4uAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbqWG_wr3KH9caZDM6Rfd_rIi0V1eIAAJotDEbbBoBSh6eSrT2N7xCAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbrWG_ws_KR0jI8scPzqMEYcgqWemOAAJptDEbbBoBSgjxW-grDpJuAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbsWG_wuJO7SE9WJ3BvTPr-jzMv7MhAAJqtDEbbBoBSl6I6_UyMWG0AQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbtWG_wvf5OvRR4lR5WyKEIQG2VCUoAAJrtDEbbBoBSiP00jFt0LZOAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbuWG_ww7cVVpje_ozVO1tSrNBiumCAAJstDEbbBoBSlfWEuWlj3AsAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbvWG_wyCXuG1aIYOQUAo0oCMuxIzNAAJttDEbbBoBSkaf_czVTG99AQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbwWG_w0iJWcSZ4JdLWTviyltMttIQAAJutDEbbBoBSuoWRrj3my_5AQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbxWG_w1rnu5B66YBa00TiYSMj1PIRAAJvtDEbbBoBStIp5wrlhNdtAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbyWG_w3IBmHpzP5eJ4p-WYBNrtqVyAAJwtDEbbBoBSsmSF_2cWBUnAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIbzWG_w4ESqG-3TMyPz4v7IHEY50bjAAJxtDEbbBoBSu4cQ7NurWsIAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIb0WG_w5GUXI_GQtJaR1xEz6v3DgABJAACcrQxG2waAUrGYxvDGK7QVQEAAwIAA3MAAyME',
            'AgACAgIAAxkBAAIb1WG_w56wr6zjlGAUs2HSPv_mQi5gAAJztDEbbBoBSgIjRo8ltMrpAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIb2WG_w61up44V4RCshAIwVt84dQUWAAJ0tDEbbBoBSlKec5khr1BwAQADAgADcwADIwQ',
            'AgACAgIAAxkBAAIb3WG_w9aakf8eB38B8Z-BElK3CFpmAAJ1tDEbbBoBSjpDmQo7RU2pAQADAgADcwADIwQ',

        ]
        photo_id = list_photo_id[random.randrange(0, len(list_photo_id), 1)]
        await self.bot.send_photo(message.chat.id, photo=photo_id)

    @info_log_message_async
    @exception
    async def process_content_new_chat_members(self, message: telebot.types.Message) -> None:
        db_worker = SQLighter(config.database_name)

        try:
            db_worker.save_id_chat(message)
        except sqlite3.IntegrityError:
            None
        db_worker.close()
        # достаем имя пользователя
        user_name = message.new_chat_member.first_name
        # выбираем рандомно одно из приветствий и отправляем в чат
        random_answer = random.randrange(0, 6, 1)
        if random_answer == 0:
            await self.bot.send_message(message.chat.id,
                                        f"Добро пожаловать, {user_name}! С новеньких по мему, местное правило (честно, всё именно так 😊)")
        elif random_answer == 1:
            await self.bot.send_message(message.chat.id,
                                        f"Привет, {user_name}! Есть местное правило - с новеньких по мему. У тебя 1 час. Потом тебя удалят (честно, всё именно так 😊)")
        elif random_answer == 2:
            await self.bot.send_message(message.chat.id,
                                        f"Добро пожаловать, {user_name}! Ваше заявление об увольнениии принято отделом кадров, для отмены пришлите мем (честно, всё именно так 😊)")
        elif random_answer == 3:
            await self.bot.send_message(message.chat.id,
                                        f"Добро пожаловать, {user_name}! Подтвердите свою личность, прислав мем в этот чат."
                                        f" Все неидентифицированные пользователи удаляются быстро - в течение 60 лет. (честно, всё именно так 😊)")
        elif random_answer == 4:
            await self.bot.send_message(message.chat.id,
                                        f"Добро пожаловать, {user_name}! К сожалению, ваше заявление на отпуск потеряно, следующий отпуск можно взять через 4 года 7 месяцев,"
                                        f"для востановления заявления пришлите мем (честно, всё именно так 😊)")
        elif random_answer == 5:
            await self.bot.send_message(message.chat.id,
                                        f" 900: {user_name},Вас приветствует Служба безопасности Сбербанка. Для отмены операции 'В фонд озеленения Луны', Сумма: 34765.00 рублей, пришлите мем "
                                        f"(честно, всё именно так 😊)")
        else:
            await self.bot.send_message(message.chat.id,
                                        f"Добро пожаловать, {user_name}! К сожалению, ваше заявление на отсрочку от мобилизации не будет принято, пока вы не пришлете мем в этот чат.")

    @info_log_message_async
    @exception
    async def process_content_photo(self, message: telebot.types.Message) -> None:
        # ЗАливка мемов в бд

        if message.caption:
            if 'send_to_chat' in message.caption.lower():
                x = message.photo[0].file_id
                if x is None:
                    return
                db_worker = SQLighter(config.database_name)
                is_admin_chat = db_worker.get_admin_chat(message)
                if is_admin_chat:
                    chat_id = is_admin_chat[0][1]
                text = str(message.caption.lower()).replace("send_to_chat", "")

                await self.bot.send_photo(chat_id, x, caption=text)
                return
            if 'load_photo_in_db' in message.caption.lower():
                x = message.photo[0].file_id
                await self.bot.send_message(message.chat.id, x)
                return
            if 'nomem' in message.caption.lower():
                return
            if 'флюгегехаймен' in message.caption.lower():
                return
        if message.from_user.username:
            db_worker = SQLighter(config.database_name)
            if db_worker.check_username_in_black_list(message.chat.id, message.from_user.username):
                return

        if message.chat.id == -532856839:
            chat_id = -1001210399850
            photo_id = message.photo[-1].file_id
            if message.chat.id == -532856839:
                await self.bot.send_message(message.chat.id, photo_id)
            #     like

            # Сохраняем фото
            file_info = await self.bot.get_file(message.photo[-1].file_id)
            downloaded_file = await self.bot.download_file(file_info.file_path)
            src = os.getcwd() + '\\image\\' + photo_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            # Получаем hash из фото
            hash_images = hash_image.CalcImageHash(src)
            # удаляем файл
            if os.path.isfile(src):
                os.remove(src)

            # Достаем словарь хэшей, если он пуст то создаем и добавляем элемент в словарь и добавляем фото в список
            db_worker = SQLighter(config.database_name)
            # запись информации о меме в бд
            rows = db_worker.select_hash_images(chat_id)
            db_worker.close()

            # Смотрим есть ли в нашем словаре такой хэш, проверяем на боян
            if str(hash_images) == '1001111111111111100000000111111110000000111111111000001111111111100111111111111111111111111111111100001000001101100000000000000011111111111111110000000001111111111111111111111110000000111111111101000011111111100000111111111111000011111111111111111111111111':
                await self.bot.send_message(message.chat.id, f"Нет сомнений, что это свежий мем!!!☝🏻")
            else:
                db_worker = SQLighter(config.database_name)
                if hash_images in rows:
                    users = db_worker.get_users_from_chat(message)
                    debt_users = []
                    for user in users:
                        ou = db_worker.check_mem_chat(message, user)
                        if ou is False:
                            debt_users.append(user)
                    await self.bot.send_message(message.chat.id,
                                                f"Похоже на этот мем... Но я всего лишь безмозглая машина @{random.choice(debt_users)} "
                                                f"поскольку ты должен мем проверь на баян.")
                    await self.bot.send_photo(message.chat.id, photo=db_worker.select_file_id(hash_images))
                    db_worker.close()

                # проверяем на 95% совпадение хэшей
                else:
                    for key in rows:

                        count = hash_image.CompareHash(key, hash_images)
                        if count < 2:
                            await self.bot.send_message(message.chat.id, f"Я сомневаюсь, но совпадение более 98%")
                            db_worker = SQLighter(config.database_name)
                            await self.bot.send_photo(message.chat.id, photo=db_worker.select_file_id(key))
                            db_worker.close()
                            break
                    # После всех проверок добаляем хеш и id изображения в словарь и в список для мемов
                    db_worker = SQLighter(config.database_name)
                    db_worker.insert_hash_image(hash_images, photo_id, chat_id)
        else:

            # достаем id изображения

            photo_id = message.photo[-1].file_id
            #     like

            user_id = message.from_user.username
            if user_id is None:
                user_id = servises.get_name(message)
            message_id = message.message_id
            chat_id = message.chat.id
            db_worker = SQLighter(config.database_name)
            data_id = 0
            # запись информации о меме в бд
            ratio_id = db_worker.creator_photo_ratio(message, photo_id, user_id, message_id, data_id, chat_id)
            db_worker.close()
            # Создаем кнопки и записываем их в переменную
            markup = types.InlineKeyboardMarkup(row_width=1)
            bt1 = types.InlineKeyboardButton(u'\U0001F49A' + ' 0', callback_data='Like_' + str(ratio_id))
            bt2 = types.InlineKeyboardButton(u'\U0001F621' + ' 0', callback_data='Dislike_' + str(ratio_id))
            markup.add(bt1, bt2)
            try:

                await self.bot.send_message(message.chat.id,
                                            'Оцени мем от @' + message.from_user.username + ' ' + u'\U0001F446',
                                            reply_markup=markup)
            except TypeError:
                if user_id is None:
                    user_id = servises.get_name(message)
                await self.bot.send_message(message.chat.id, 'Оцени мем от ' + user_id + ' ' + u'\U0001F446',
                                            reply_markup=markup, parse_mode="Markdown")
            except:
                img = open('animation.gif.mp4', 'rb')
                await self.bot.send_video(message.chat.id, img)
                img.close()
            # Сохраняем фото
            file_info = await self.bot.get_file(message.photo[-1].file_id)
            downloaded_file = await self.bot.download_file(file_info.file_path)
            src = os.getcwd() + '\\image\\' + photo_id
            with open(src, 'wb') as new_file:
                new_file.write(downloaded_file)
            # Получаем hash из фото
            hash_images = hash_image.CalcImageHash(src)
            # удаляем файл
            if os.path.isfile(src):
                os.remove(src)

            # Достаем словарь хэшей, если он пуст то создаем и добавляем элемент в словарь и добавляем фото в список
            db_worker = SQLighter(config.database_name)
            # запись информации о меме в бд
            rows = db_worker.select_hash_images(message.chat.id)
            db_worker.close()

            # Смотрим есть ли в нашем словаре такой хэш, проверяем на боян
            if str(hash_images) == '1001111111111111100000000111111110000000111111111000001111111111100111111111111111111111111111111100001000001101100000000000000011111111111111110000000001111111111111111111111110000000111111111101000011111111100000111111111111000011111111111111111111111111':
                await self.bot.send_message(message.chat.id, f"Нет сомнений, что это свежий мем!!!☝🏻")
            else:
                db_worker = SQLighter(config.database_name)
                if hash_images in rows:
                    users = db_worker.get_users_from_chat(message)
                    debt_users = []
                    for user in users:
                        ou = db_worker.check_mem_chat(message, user)
                        if ou is False:
                            debt_users.append(user)
                    await self.bot.send_message(message.chat.id,
                                                f"Похоже на этот мем... Но я всего лишь безмозглая машина @{random.choice(debt_users)} "
                                                f"поскольку ты должен мем проверь на баян.")
                    await self.bot.send_photo(message.chat.id, photo=db_worker.select_file_id(hash_images))
                    db_worker.close()

                # проверяем на 95% совпадение хэшей
                else:
                    for key in rows:

                        count = hash_image.CompareHash(key, hash_images)
                        if count < 2:
                            db_worker = SQLighter(config.database_name)

                            users = db_worker.get_users_from_chat(message)
                            debt_users = []
                            for user in users:
                                ou = db_worker.check_mem_chat(message, user)
                                if ou is False:
                                    debt_users.append(user)
                            await self.bot.send_message(message.chat.id,
                                                        f"Похоже на этот мем... Но я всего лишь безмозглая машина @{random.choice(debt_users)} "
                                                        f"поскольку ты должен мем проверь на баян.")
                            await self.bot.send_photo(message.chat.id, photo=db_worker.select_file_id(hash_images))
                            db_worker.close()
                            break
                    # После всех проверок добаляем хеш и id изображения в словарь и в список для мемов
                    db_worker = SQLighter(config.database_name)
                    db_worker.insert_hash_image(hash_images, photo_id, message.chat.id)
                    answer = utils.get_answer_for_user(message.chat.id)
                    if answer == None:
                        answer = []
                        answer.append(photo_id)
                        utils.set_id_photo_for_chat(message.chat.id, answer)
                    else:
                        # chat_id memes_guild = -1001210399850
                        if message.chat.id == -532856839:
                            message.chat.id = -1001210399850
                            answer = utils.get_answer_for_user(message.chat.id)
                            answer.append(photo_id)
                            utils.set_id_photo_for_chat(message.chat.id, answer)
                        else:
                            answer.append(photo_id)
                            utils.set_id_photo_for_chat(message.chat.id, answer)

    @info_log_message_async
    @exception
    async def process_content_video(self, message: telebot.types.Message) -> None:
        if message.caption:
            if 'nomem' in message.caption.lower():
                return
            if 'флюгегехаймен' in message.caption.lower():
                return
        video_id = message.video.file_id
        if message.chat.id == -532856839:
            await self.bot.send_message(message.chat.id, video_id)
        chat_id = message.chat.id
        user_id = message.from_user.username
        if user_id is None:
            user_id = servises.get_name(message)
        message_id = message.message_id
        data_id = 1
        db_worker = SQLighter(config.database_name)
        # запись информации о меме в бд
        ratio_id = db_worker.creator_photo_ratio(message, video_id, user_id, message_id, data_id, chat_id)
        db_worker.close()
        # Создаем кнопки и записываем их в переменную
        markup = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton(u'\U0001F49A' + ' 0', callback_data='Like_' + str(ratio_id))
        bt2 = types.InlineKeyboardButton(u'\U0001F621' + ' 0', callback_data='Dislike_' + str(ratio_id))
        markup.add(bt1, bt2)
        try:
            await self.bot.send_message(message.chat.id,
                                        'Оцени мем от @' + message.from_user.username + ' ' + u'\U0001F446',
                                        reply_markup=markup)
        except TypeError:
            if user_id is None:
                user_id = servises.get_name(message)
            await self.bot.send_message(message.chat.id, 'Оцени мем от ' + user_id + ' ' + u'\U0001F446',
                                        reply_markup=markup, parse_mode="Markdown")
        except:
            img = open('animation.gif.mp4', 'rb')
            await self.bot.send_video(message.chat.id, img)
            img.close()

    @info_log_message_async
    @exception
    async def process_get_text_messages(self, message: telebot.types.Message) -> None:

        m = str(message).replace("'", '"').replace('False', '"False"').replace('True', '"True"').replace('null',
                                                                                                         '"null"').replace(
            'None', '"None"')
        n = json.dumps(m)
        o = json.loads(n)
        d = {"message_": o}
        logging.info('User Message', extra=d)
        db_worker = SQLighter(config.database_name)

        try:
            db_worker.save_id_chat(message)
        except sqlite3.IntegrityError:
            None
        db_worker.close()
        if message.text == "Как тебе мем?":
            photo_id = 'AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E'

            await self.bot.send_photo(message.chat.id, photo=photo_id)

    @info_log_message_async
    @exception
    async def get_data(self, request: object) -> web.Response:
        """

        :param request:
        :return:
        Updates information about new messages for the bot
        """
        pass

    @exception
    async def run(self) -> None:
        """

        :return:
        Running bot polling
        """
        await self.bot.remove_webhook()

        await self.bot.polling(non_stop=True, skip_pending=True, timeout=40, request_timeout=40)  # to skip updates

    @exception
    async def run_webhook(self) -> None:
        """
        Running bot webhooks
        """

        await self.bot.run_webhooks(
            listen=WEBHOOK_HOST,
            port=WEBHOOK_PORT,
            url_path=WEBHOOK_URL_PATH,
            certificate=WEBHOOK_SSL_CERT,
            certificate_key=WEBHOOK_SSL_PRIV
        )


# Depending on the settings, select the type of connection
if webhook is True:
    core = Core()
    asyncio.run(
        core.run_webhook())

else:
    if __name__ == '__main__':
        core = Core()
        asyncio.run(core.run())
