# -*- coding: utf-8 -*-
import shelve

import telebot
import config

from config import shelve_name, shelve_level

bot = telebot.TeleBot(config.token)

def set_id_photo_for_chat(chat_id, args):
    """

    """
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)] = args



def get_id_photo_for_chat(chat_id):
    """

    """
    with shelve.open(shelve_name) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None


def set_hash_photo_for_chat(chat_id, args):
    """

    """
    with shelve.open(shelve_level) as storage:
        storage[str(chat_id)] = args



def get_hush_photo_for_chat(chat_id):
    """

    """
    with shelve.open(shelve_level) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None









def get_answer_for_user(chat_id):
    """

    """
    with shelve.open(shelve_name) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None



