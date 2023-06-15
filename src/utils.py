# -*- coding: utf-8 -*-
import shelve

import telebot
import config

from config import SHELVE_NAME, SHELVE_LEVEL


def set_id_photo_for_chat(chat_id, args):
    """

    """
    with shelve.open(SHELVE_NAME) as storage:
        storage[str(chat_id)] = args


def get_id_photo_for_chat(chat_id):
    """

    """
    with shelve.open(SHELVE_NAME) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None


def set_hash_photo_for_chat(chat_id, args):
    """

    """
    with shelve.open(SHELVE_LEVEL) as storage:
        storage[str(chat_id)] = args



def get_hush_photo_for_chat(chat_id):
    """

    """
    with shelve.open(SHELVE_LEVEL) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None









def get_answer_for_user(chat_id):
    """

    """
    with shelve.open(SHELVE_NAME) as storage:
        try:
            answer = storage[str(chat_id)]
            return answer
        except KeyError:
            return None



