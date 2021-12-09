# -*- coding: utf-8 -*-
'''Github Action rules'''

# @pirog - telegram
import json
import os
import random
import re
import ssl

from datetime import datetime
import logging.config
import flask
from aiohttp import web
import logging
import time
import utils
import config
import env
import telebot
from telebot import types
import hash_image
from SQLighter import SQLighter
from gevent.pywsgi import WSGIServer
from pythonjsonlogger import jsonlogger


bot = telebot.TeleBot(env.token)
WEBHOOK_HOST = '217.163.29.237'
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '217.163.29.237'  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = '/home/lukas/cert/webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = '/home/lukas/cert/webhook_pkey.pem'  # Path to the ssl private key
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (env.token)
#
# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)


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


# для вебхуков flask

# app = flask.Flask(__name__)
#
#
# # Empty webserver index, return nothing, just http 200
# @app.route('/', methods=['GET', 'HEAD'])
# def index():
#     return ''
#
#
# # Process webhook calls
# @app.route(WEBHOOK_URL_PATH, methods=['POST'])
# def webhook():
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         flask.abort(403)
#
#


""""
отправка мема в чат
"""


@bot.message_handler(commands=['mem'])
def lession(message):
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
def lession(message):
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
def lession(message):
    if message.chat.id == -532856839:
        chat_id = -1001210399850

        bot.send_message(chat_id,
                         f"Зарплатонька пришла! <3")
        video_id = 'BAACAgIAAxkBAAIF7WETfRw8K1_iDaks2SY9TnhRMtmYAALBEQACEs2ZSDzrW4IZoA1wIAQ'
        bot.send_video(chat_id, video_id)
    else:

        bot.send_message(message.chat.id,
                         f"Зарплатонька пришла!")
        video_id = 'BAACAgIAAxkBAAIF7WETfRw8K1_iDaks2SY9TnhRMtmYAALBEQACEs2ZSDzrW4IZoA1wIAQ'
        bot.send_video(message.chat.id, video_id)


@bot.message_handler(commands=['gud'])
def get_text_messages(message):
    if message.chat.id == -532856839:
        # Отсылаем в чат
        message.chat.id = -1001210399850
        # AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E

        photo_id = 'AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E'

        bot.send_photo(message.chat.id, photo=photo_id)

    else:
        None


"""
Приветствие вновь прибывших
"""


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
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
    data = c.data
    clear_data = re.sub(r'[^\w\s]+|[\d]+', r'', data).strip()
    if clear_data == 'Like_':

        callback_ratio_id = (int(''.join(filter(str.isdigit, data))))

        user_id = c.from_user.username
        if user_id is None:
            bot.answer_callback_query(c.id, text='Вам необходимо заполнить username, что бы голосовать')
            return

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
            bot.answer_callback_query(c.id, text='Вам необходимо заполнить username, что бы голосовать')
            return

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


"""Сбор фото мемов"""


@bot.message_handler(content_types=['photo'])
def handle_docs_audio(message):
    # ЗАливка мемов в бд

    if message.chat.id == -532856839:
        chat_id = -1001210399850
        photo_id = message.photo[-1].file_id
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
        else:
            None

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
                        bot.send_message(message.chat.id, f"Я сомневаюсь, но  совпадение более 98%")
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
        message_id = message.message_id
        chat_id=message.chat.id
        db_worker = SQLighter(config.database_name)
        data_id=0
        # запись информации о меме в бд
        ratio_id = db_worker.creator_photo_ratio(message, photo_id, user_id, message_id, data_id, chat_id)
        db_worker.close()
        # Создаем кнопки и записываем их в переменную
        markup = types.InlineKeyboardMarkup(row_width=1)
        bt1 = types.InlineKeyboardButton(u'\U0001F49A' + ' 0', callback_data='Like_' + str(ratio_id))
        bt2 = types.InlineKeyboardButton(u'\U0001F621' + ' 0', callback_data='Dislike_' + str(ratio_id))
        markup.add(bt1, bt2)
        try:

            bot.send_message(message.chat.id, 'Оцени мем от @' + user_id + ' ' + u'\U0001F446',
                         reply_markup=markup)
        except TypeError:
            bot.send_message(message.chat.id, 'Главное помнить, что ты никому ничего не должен')
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
        else:
            None

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
                        bot.send_message(message.chat.id, f"Я сомневаюсь, но  совпадение более 98%")
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
def get_text_messges(message):
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
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе')

    else:
        chat_id=message.chat.id
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
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе',
                                 reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе')
            elif int(data_id) == 1:
                bot.send_video(message.chat.id, data = photo_id)
                try:
                    bot.send_message(message.chat.id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе',
                                 reply_to_message_id=message_id)
                except:
                    bot.send_message(message.chat.id,
                                 f' @{username}  Твой мем набрал {ratio} лайков - больше всех  на этой неделе')
        except IndexError:
            bot.send_message(message.chat.id,
                             f'Нет ни одного мема в базе')


@bot.message_handler(commands=['top30'])
def get_text_messges(message):
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
        chat_id= message.chat.id
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
def get_text_messages(message):
    video_id = message.video.file_id
    chat_id = message.chat.id
    user_id = message.from_user.username
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
        bot.send_message(message.chat.id, 'Оцени мем от @' + user_id + ' ' + u'\U0001F446',
                     reply_markup=markup)
    except TypeError:
        bot.send_message(message.chat.id, 'Для участие в рейтинге необходимо заполнить Имя пользователя')

@bot.message_handler(commands=['tophunya7'])
def get_text_messges(message):
    chat_id=message.chat.id
    mem_chat= -1001210399850
    db_worker = SQLighter(config.database_name)
    top = db_worker.ratio_rating_3_7days(mem_chat)
    db_worker.close()
    i=0

    for el in top:

        ratio = top[i][1]
        photo_id = top[i][2]
        username = top[i][3]
        message_id = top[i][5]
        data_id = top[i][7]
        i=i+1
        if int(data_id) == 0:
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username} '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех  на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех  на этой неделе')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех  на этой неделе',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех  на этой неделе')

@bot.message_handler(commands=['tophunya30'])
def get_text_messges(message):
    chat_id=message.chat.id
    mem_chat= -1001210399850

    db_worker = SQLighter(config.database_name)
    top = db_worker.ratio_rating_3_7days(mem_chat)
    db_worker.close()
    i=0

    for el in top:

        ratio = top[i][1]
        photo_id = top[i][2]
        username = top[i][3]
        message_id = top[i][5]
        data_id = top[i][7]
        i=i+1
        if int(data_id) == 0:
            bot.send_photo(chat_id, photo=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username} '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце')
        elif int(data_id) == 1:
            bot.send_video(chat_id, data=photo_id)
            try:
                bot.send_message(chat_id,
                                 f' @{username}  '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце',
                                 reply_to_message_id=message_id)
            except:
                bot.send_message(chat_id,
                                 f' @{username}  '+ str(i) +f' Место. Твой мем набрал {ratio} лайков - больше всех в этом месяце')


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

    m = str(message).replace("'", '"').replace('False', '"False"').replace('True', '"True"').replace('null', '"null"').replace('None', '"None"')
    n = json.dumps(m)
    o = json.loads(n)
    d={"message_" : o}
    logging.info('User Message', extra=d)

    if message.text == "Как тебе мем?":
        photo_id = 'AgACAgIAAx0CSCU8agACDUtgwOcC6LjfltASaCFDKTlrL3xkKwACRLQxG36qCUrKMzSvBkjb_ooQZ5MuAAMBAAMCAANzAAMKNQIAAR8E'

        bot.send_photo(message.chat.id, photo=photo_id)
    else:
        None


if config.webhook is True:
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


# для вебхуков flask
# if env.webhook == True:
#
#     time.sleep(1)
#     # app.config['ENV']='development'
#     # Set webhook
#     bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
#                     certificate=open(WEBHOOK_SSL_CERT, 'r'))
#
#     # Start flask server
#     app.run(host=WEBHOOK_LISTEN,
#             port=WEBHOOK_PORT,
#             ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
#             debug=False)
# else:
#
#     if __name__ == '__main__':
#         bot.remove_webhook()
#
#         bot.polling(none_stop=True)
