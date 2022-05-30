# -*- coding: utf-8 -*-
"""Github Action rules"""
from datetime import datetime

"""@pirog - telegram"""
import json
import os
import random
import re
import sqlite3
import ssl

import logging.config
from aiohttp import web
import logging
import requests

import servises
import utils
import config
import env
import telebot
from telebot import types
import hash_image
from SQLighter import SQLighter
from pythonjsonlogger import jsonlogger
from wednesday import IMAGES

bot = telebot.TeleBot(env.token)
WEBHOOK_HOST = '217.163.29.237'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '217.163.29.237'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = '/home/lukas/cert/webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = '/home/lukas/cert/webhook_pkey.pem'  # Path to the ssl private key
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (env.token)
#


logger = logging.getLogger(__name__)
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
answerlog = logging.config.fileConfig('logging-json.ini', disable_existing_loggers=False)

app = web.Application()


# Process webhook calls
async def handle(request):
    if request.match_info.get('token') == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        bot.process_new_updates([update])
        return web.Response()
    else:
        return web.Response(status=403)


app.router.add_post('/{token}/', handle)

""""
отправка мема в чат
"""


@bot.message_handler(commands=['wednesday'])
def happy_1(message):
    now = datetime.now()
    day_now = datetime.isoweekday(now)

    URL = IMAGES[day_now.__str__()][random.randint(0, len(IMAGES[day_now.__str__()]) - 1)]
    response = requests.get(URL)
    src = os.getcwd() + '\\image\\' + str(message.date) + '.jpeg';
    open(src, "wb").write(response.content)
    immagesss = open(src, 'rb')
    bot.send_photo(message.chat.id, immagesss)
    del immagesss
    if os.path.isfile(src):
        os.remove(src)



@bot.message_handler(commands=['mem'])
def get_mem(message):
    if message.chat.id == -532856839:
        chat_id = -1001210399850
        x = utils.get_id_photo_for_chat(chat_id)

        if x == None: return
        # Выбираем случайный элемент списка
        photo_id = x[random.randrange(0, len(x), 1)]
        # Отсылаем в чат
        bot.send_photo(chat_id, photo=photo_id)
    else:
        x = utils.get_id_photo_for_chat(message.chat.id)

        if x == None: return
        # Выбираем случайный элемент списка
        photo_id = x[random.randrange(0, len(x), 1)]
        # Отсылаем в чат
        bot.send_photo(message.chat.id, photo=photo_id)


@bot.message_handler(commands=['happy1'])
def happy_1(message):
    if message.chat.id == -532856839:
        chat_id = -1001210399850

        bot.send_message(chat_id,
                         f"Зарплатонька пришла! <3")
        video_id = 'BAACAgIAAxkBAAIEcmDZoRe-LA3QzjetEJdOTezCAAGu5wACpgoAAmt1WEo3ZqrbnJ8IkyAE'
        bot.send_video(chat_id, video_id)
    else:

        bot.send_message(message.chat.id,
                         f"Зарплатонька пришла!")
        video_id = 'BAACAgIAAxkBAAIEcmDZoRe-LA3QzjetEJdOTezCAAGu5wACpgoAAmt1WEo3ZqrbnJ8IkyAE'
        bot.send_video(message.chat.id, video_id)


@bot.message_handler(commands=['happy2'])
def happy_2(message):
    if message.chat.id == -532856839:
        chat_id = -1001210399850

        bot.send_message(chat_id,
                         f"Зарплатонька пришла! <3")
        video_id = 'BAACAgIAAxkBAAIi5GIDtRHNy4EMZvOoq712hREwZ66kAAITEgAC6feYSDxMbJ2_DrFOIwQ'
        bot.send_video(chat_id, video_id)
    else:

        bot.send_message(message.chat.id,
                         f"Зарплатонька пришла!")
        video_id = 'BAACAgIAAxkBAAIi5GIDtRHNy4EMZvOoq712hREwZ66kAAITEgAC6feYSDxMbJ2_DrFOIwQ'
        bot.send_video(message.chat.id, video_id)


@bot.message_handler(commands=['happy3'])
def happy_2(message):
    if message.chat.id == -532856839:
        chat_id = -1001210399850

        bot.send_message(chat_id,
                         f"Зарплатонька пришла! <3")
        video_id = 'BAACAgIAAxkBAAIlFmJTTJgx0ZO7Tvp3KRVYLJuyNT4dAAIDGgACs1OYSlyrbCsG6j6EIwQ'
        bot.send_video(chat_id, video_id)
    else:

        bot.send_message(message.chat.id,
                         f"Зарплатонька пришла!")
        video_id = 'BAACAgIAAxkBAAIlFmJTTJgx0ZO7Tvp3KRVYLJuyNT4dAAIDGgACs1OYSlyrbCsG6j6EIwQ'
        bot.send_video(message.chat.id, video_id)


@bot.message_handler(commands=['gud'])
def good_message(message):
    if message.chat.id == -532856839:
        # Отсылаем в чат
        message.chat.id = -1001210399850
        # AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E

        photo_id = 'AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E'

        bot.send_photo(message.chat.id, photo=photo_id)


"""
Приветствие вновь прибывших
"""


@bot.message_handler(content_types=["new_chat_members"])
def hi_new_member(message):
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
        bot.send_message(message.chat.id,
                         f"Добро пожаловать, {user_name}! С новеньких по мему, местное правило (честно, всё именно так 😊)")
    elif random_answer == 1:
        bot.send_message(message.chat.id,
                         f"Привет, {user_name}! Есть местное правило - с новеньких по мему. У тебя 1 час. Потом тебя удалят (честно, всё именно так 😊)")
    elif random_answer == 2:
        bot.send_message(message.chat.id,
                         f"Добро пожаловать, {user_name}! Ваше заявление об увольнениии принято отделом кадров, для отмены пришлите мем (честно, всё именно так 😊)")
    elif random_answer == 3:
        bot.send_message(message.chat.id,
                         f"Добро пожаловать, {user_name}! Подтвердите свою личность, прислав мем в этот чат."
                         f" Все неидентифицированные пользователи удаляются быстро - в течение 60 лет. (честно, всё именно так 😊)")
    elif random_answer == 4:
        bot.send_message(message.chat.id,
                         f"Добро пожаловать, {user_name}! К сожалению, ваше заявление на отпуск потеряно, следующий отпуск можно взять через 4 года 7 месяцев,"
                         f"для востановления заявления пришлите мем (честно, всё именно так 😊)")
    elif random_answer == 5:
        bot.send_message(message.chat.id,
                         f" 900: {user_name},Вас приветствует Служба безопасности Сбербанка. Для отмены операции 'В фонд озеленения Луны', Сумма: 34765.00 рублей, пришлите мем "
                         f"(честно, всё именно так 😊)")
    else:
        bot.send_message(message.chat.id,
                         f"Добро пожаловать, {user_name}! К сожалению, ваше заявление на отпуск потеряно, следующий отпуск можно взять через 4 года 7 месяцев,"
                         f"для востановления заявления пришлите мем (честно, всё именно так 😊)")


@bot.callback_query_handler(func=lambda c: True)
def callback(c):
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

        if like == True:
            db_worker.update_ratio_like_off(callback_ratio_id)
            db_worker.update_ratio_to_like_off(callback_ratio_id, user_id)
            ratio_value = db_worker.select_ratio_value(callback_ratio_id)
            ratio_dislike_value = db_worker.select_ratio_dislike_value(callback_ratio_id)
            db_worker.close()

            ratio_value = u'\U0001F49A' + ' ' + str(ratio_value)
            ratio_dislike_value = u'\U0001F621' + ' ' + str(ratio_dislike_value)
            markup = types.InlineKeyboardMarkup(row_width=1)
            bt1 = types.InlineKeyboardButton(ratio_value, callback_data='Like_' + str(callback_ratio_id))
            bt2 = types.InlineKeyboardButton(ratio_dislike_value, callback_data='Dislike_' + str(callback_ratio_id))

            markup.add(bt1, bt2)
            bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=markup)
            bot.answer_callback_query(c.id, text='Ваш голос убран')

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
            bt2 = types.InlineKeyboardButton(ratio_dislike_value, callback_data='Dislike_' + str(callback_ratio_id))

            markup.add(bt1, bt2)
            bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=markup)
            bot.answer_callback_query(c.id, text='Ваш голос учтен')

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
            bt2 = types.InlineKeyboardButton(ratio_dislike_value, callback_data='Dislike_' + str(callback_ratio_id))

            markup.add(bt1, bt2)
            bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=markup)

            bot.answer_callback_query(c.id, text='Ваш голос убран')
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
            bt2 = types.InlineKeyboardButton(ratio_dislike_value, callback_data='Dislike_' + str(callback_ratio_id))

            markup.add(bt1, bt2)
            bot.edit_message_reply_markup(c.message.chat.id, c.message.message_id, reply_markup=markup)
            bot.answer_callback_query(c.id, text='Ваш голос учтен')

            # bot.answer_callback_query(c.message.chat.id, 'Конфиг пуст', reply_markup=markup)
    if data == 'get_groshi':
        bot.answer_callback_query(c.id, text='Грошi высланы на счет')


"""Сбор фото мемов"""


@bot.message_handler(commands=["cash"])
def games_editor_1(message, ):
    # Смотрим есть ли сохраненый ранее конфиг у пользователей

    # Создаем кнопки и записываем их в переменную
    start_markup = telebot.types.InlineKeyboardMarkup()

    # первый ряд (две кнопки)
    btn0 = telebot.types.InlineKeyboardButton('Дайте грошi', callback_data='get_groshi')
    start_markup.row(btn0)
    bot.send_message(message.chat.id, 'Шо надо?',
                     reply_markup=start_markup)


@bot.message_handler(content_types=['photo'])
def set_photo(message):
    # ЗАливка мемов в бд
    if message.caption == 'nomem':
        return
    if message.chat.id == -532856839:
        chat_id = -1001210399850
        photo_id = message.photo[-1].file_id
        if message.chat.id == -532856839:
            bot.send_message(message.chat.id, photo_id)
        #     like

        # Сохраняем фото
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = os.getcwd() + '\\image\\' + photo_id;
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
            bot.send_message(message.chat.id, f"Нет сомнений, что это свежий мем!!!☝🏻")
        else:
            if hash_images in rows:
                bot.send_message(message.chat.id, f"Алярм!!! Походу баян...")
                db_worker = SQLighter(config.database_name)
                bot.send_photo(message.chat.id, photo=db_worker.select_file_id(hash_images))
                db_worker.close()

            # проверяем на 95% совпадение хэшей
            else:
                for key in rows:

                    count = hash_image.CompareHash(key, hash_images)
                    if count < 2:
                        bot.send_message(message.chat.id, f"Я сомневаюсь, но совпадение более 98%")
                        db_worker = SQLighter(config.database_name)
                        bot.send_photo(message.chat.id, photo=db_worker.select_file_id(key))
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

            bot.send_message(message.chat.id, 'Оцени мем от @' + message.from_user.username + ' ' + u'\U0001F446',
                             reply_markup=markup)
        except TypeError:
            if user_id is None:
                user_id = servises.get_name(message)
            bot.send_message(message.chat.id, 'Оцени мем от ' + user_id + ' ' + u'\U0001F446',
                             reply_markup=markup, parse_mode="Markdown")
        except:
            img = open('animation.gif.mp4', 'rb')
            bot.send_video(message.chat.id, img)
            img.close()
        # Сохраняем фото
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = os.getcwd() + '\\image\\' + photo_id;
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
            bot.send_message(message.chat.id, f"Нет сомнений, что это свежий мем!!!☝🏻")
        else:
            if hash_images in rows:
                bot.send_message(message.chat.id, f"Алярм!!! Походу баян...")
                db_worker = SQLighter(config.database_name)
                bot.send_photo(message.chat.id, photo=db_worker.select_file_id(hash_images))
                db_worker.close()

            # проверяем на 95% совпадение хэшей
            else:
                for key in rows:

                    count = hash_image.CompareHash(key, hash_images)
                    if count < 2:
                        bot.send_message(message.chat.id, f"Я сомневаюсь, но совпадение более 98%")
                        db_worker = SQLighter(config.database_name)
                        bot.send_photo(message.chat.id, photo=db_worker.select_file_id(key))
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


""""Меню старт"""


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Для Гильдии Python")


@bot.message_handler(commands=['top7'])
def top_7(message):
    if message.chat.id == -1001210399850:
        return
    elif message.chat.id == -532856839:
        chat_id = -1001210399850
        db_worker = SQLighter(config.database_name)
        top = db_worker.ratio_rating_7days(chat_id)
        db_worker.close()

        ratio = top[1]
        photo_id = top[2]
        username = top[3]
        message_id = top[5]
        data_id = top[7]

        if int(data_id) == 0:
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
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
                bot.send_photo(message.chat.id, photo=photo_id)
                try:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
            elif int(data_id) == 1:
                bot.send_video(message.chat.id, data=photo_id)
                try:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
        except IndexError:
            bot.send_message(message.chat.id,
                             f'Нет ни одного мема в базе')


@bot.message_handler(commands=['top30'])
def top_30(message):
    if message.chat.id == -1001210399850:
        return
    elif message.chat.id == -532856839:
        chat_id = -1001210399850
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
                bot.send_photo(chat_id, photo=photo_id)
                try:
                    bot.send_message(chat_id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(chat_id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
            elif int(data_id) == 1:
                bot.send_video(chat_id, data=photo_id)
                try:
                    bot.send_message(chat_id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(chat_id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
        except IndexError:
            bot.send_message(message.chat.id,
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
                bot.send_photo(message.chat.id, photo=photo_id)
                try:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
            elif int(data_id) == 1:
                bot.send_video(message.chat.id, data=photo_id)
                try:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - он лучший в этом месяце! Поздравляю!')
        except IndexError:
            bot.send_message(message.chat.id,
                             f'Нет ни одного мема в базе')


@bot.message_handler(content_types=['video'])
def set_viseo(message):
    video_id = message.video.file_id
    if message.chat.id == -532856839:
        bot.send_message(message.chat.id, video_id)
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
        bot.send_message(message.chat.id, 'Оцени мем от @' + message.from_user.username + ' ' + u'\U0001F446',
                         reply_markup=markup)
    except TypeError:
        if user_id is None:
            user_id = servises.get_name(message)
        bot.send_message(message.chat.id, 'Оцени мем от ' + user_id + ' ' + u'\U0001F446',
                         reply_markup=markup, parse_mode="Markdown")
    except:
        img = open('animation.gif.mp4', 'rb')
        bot.send_video(message.chat.id, img)
        img.close()


@bot.message_handler(commands=['tophunya7'])
def top_hunya_7(message):
    chat_id = message.chat.id
    mem_chat = -1001210399850
    db_worker = SQLighter(config.database_name)
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
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username} ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')


@bot.message_handler(commands=['tophunya30'])
def top_hunya_30(message):
    chat_id = message.chat.id
    mem_chat = -1001210399850

    db_worker = SQLighter(config.database_name)
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
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username} ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце')


@bot.message_handler(commands=['tophunya'])
def top_hunya(message):
    chat_id = message.chat.id
    mem_chat = -1001210399850
    db_worker = SQLighter(config.database_name)
    top = db_worker.ratio_rating_all_time(mem_chat)
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
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username} ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Место. Твой мем набрал {ratio} лайков - больше всех на этой неделе')


@bot.message_handler(commands=['top'])
def top(message):
    if message.chat.id == -1001210399850:
        return
    elif message.chat.id == -532856839:
        chat_id = -1001210399850
        db_worker = SQLighter(config.database_name)
        top = db_worker.ratio_rating_all_time_for_top(chat_id)
        db_worker.close()

        ratio = top[1]
        photo_id = top[2]
        username = top[3]
        message_id = top[5]
        data_id = top[7]

        if int(data_id) == 0:
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех за все время',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
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
                bot.send_photo(message.chat.id, photo=photo_id)
                try:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
            elif int(data_id) == 1:
                bot.send_video(message.chat.id, data=photo_id)
                try:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе',
                                     reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                     f' @{username}  Твой мем набрал {ratio} лайков - больше всех на этой неделе')
        except IndexError:
            bot.send_message(message.chat.id,
                             f'Нет ни одного мема в базе')


@bot.message_handler(commands=['antitophunya'])
def anti_top_hunya(message):
    chat_id = message.chat.id
    mem_chat = -1001210399850
    db_worker = SQLighter(config.database_name)
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
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username} ' + str(
                                     i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  ' + str(
                                     i) + f' Ты набрал больше всего дизлайков {ratio}. Ну и душнила!')


@bot.message_handler(commands=['helper'])
def help(message):
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
           f'/load узнать photo_id\n' \
           f'\n' \
           f'/send_to_chat отправить фото в чат мемов (для отмены сообщение "стоп")\n' \
           f'\n' \
           f'/toplionhunya - все самолайки' \
           f'\n' \
           f'/debt долги по мемам' \
           f'\n' \
        # \
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['send_to_chat'])
def send_photo_to_chat(message):
    msgPrice = bot.send_message(message.chat.id, 'Присылай фото:')
    bot.register_next_step_handler(msgPrice, servises.send_to_chat)


@bot.message_handler(commands=['load'])
def load_photo(message):
    msgPrice = bot.send_message(message.chat.id, 'Присылай фото:')
    bot.register_next_step_handler(msgPrice, servises.get_photo_id)


@bot.message_handler(commands=['f'])
def set_f(message):
    print(message.chat.id)
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
    bot.send_photo(message.chat.id, photo=photo_id)


@bot.message_handler(commands=['toplionhunya'])
def set_top_lion(message):
    # starttime = time.time()
    if message.chat.id == -532856839:
        message.chat.id = -1001210399850
        chat_id = -532856839
    db_worker = SQLighter(config.database_name)
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

    bot.send_message(chat_id, top_lion_str)
    # endtime = time.time()
    # duration = endtime - starttime


@bot.message_handler(commands=['debt'])
def set_f(message):
    if message.chat.id == -532856839:
        message.chat.id = -1001210399850
        chat_id = -532856839
    db_worker = SQLighter(config.database_name)
    users = db_worker.get_users_from_chat(message)
    debt_users = []
    for user in users:
        ou = db_worker.check_mem_chat(message, user)
        if ou is False:
            debt_users.append(user)
    db_worker.close()

    if bool(debt_users) is False: return bot.send_message(chat_id, 'Долгов нет')
    debt_users_str = ''

    for debt in debt_users:
        debt_users_str = debt_users_str + '@ ' + str(debt) + f' \n'

    bot.send_message(chat_id, debt_users_str)


@bot.message_handler(commands=['message'])
def start1(message):
    if message.chat.id == -532856839:
        # Отсылаем в чат
        message.chat.id = -1001210399850
        text = message.text[9:]
        bot.send_message(message.chat.id, text)
    else:
        text = message.text[9:]

        bot.send_message(message.chat.id, text)


# @bot.message_handler(commands=['hash_download'])
# def start1(message):
#     rows = utils.get_hush_photo_for_chat(message.chat.id)
#     for key in rows.keys():
#         bot.send_photo(message.chat.id, photo=rows[key])
#         file_info = bot.get_file(rows[key])
#         downloaded_file = bot.download_file(file_info.file_path)
#         src = os.getcwd() + '\\image2\\' + rows[key] + '.jpg';
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)
#
# @bot.message_handler(commands=['hash_sendphoto'])
# def start1(message):
#     rows = utils.get_hush_photo_for_chat(message.chat.id)
#     for key in rows.keys():
#         bot.send_photo(message.chat.id, photo=rows[key])
#
# @bot.message_handler(commands=['hash_sendphoto_from_memchat'])
# def start1(message):
#     rows = utils.get_hush_photo_for_chat(-1001210399850)
#     i=0
#     for key in rows.keys():
#         if i <1198:
#             i+=1
#         else:
#
#             if i % 20 ==0:
#                 time.sleep(3)
#                 bot.send_photo(message.chat.id, photo=rows[key])
#                 i+=1
#             else:
#                 bot.send_photo(message.chat.id, photo=rows[key])
#                 i+=1
#
#
# @bot.message_handler(commands=['hash_len_memchat'])
# def start1(message):
#     rows = utils.get_hush_photo_for_chat(-1001210399850)
#     bot.send_message(message.chat.id, len(rows))
#
# @bot.message_handler(commands=['hash_len'])
# def start1(message):
#     rows = utils.get_hush_photo_for_chat(message.chat.id)
#     bot.send_message(message.chat.id, len(rows))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
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

        bot.send_photo(message.chat.id, photo=photo_id)


if env.webhook is True:
    # Set webhook
    bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                    certificate=open(WEBHOOK_SSL_CERT, 'r'))

    # Build ssl context
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV)

    # Start aiohttp server
    web.run_app(
        app,
        host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=context,
    )
else:
    if __name__ == '__main__':
        bot.remove_webhook()

        bot.polling(none_stop=True)
