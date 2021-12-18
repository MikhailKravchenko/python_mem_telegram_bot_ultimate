# -*- coding: utf-8 -*-
import sqlite3
import sys
from datetime import datetime


class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def creator_photo_ratio(self, message, photo_id, user_id, message_id, data_id, chat_id):

        with self.connection:

            self.cursor.execute(
                'INSERT INTO ratio (photo_id, user_id, create_time, message_id, data_id, chat_id) VALUES (''\'' + str(
                    photo_id) + '\',\'' + str(
                    user_id) + '\',\'' +
                str(
                    datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')) + '\',\'' + str(
                    message_id) + '\',\'' + str(data_id) + '\',\'' + str(chat_id) + '\''')')

        ratio_id = self.cursor.execute('SELECT last_insert_rowid()').fetchall()

        for ratio in ratio_id:
            for ratio_id in ratio:
                ratio_id = ratio_id
        return ratio_id

        return ratio_id

    def update_ratio_like(self, ratio_id):
        with self.connection:
            self.cursor.execute(
                'UPDATE ratio set ratio_value =ratio_value+ 1 where ratio_id=' + str(ratio_id))

    def update_ratio_like_off(self, ratio_id):
        with self.connection:
            self.cursor.execute(
                'UPDATE ratio set ratio_value =ratio_value- 1 where ratio_id=' + str(ratio_id))

    def update_ratio_dislike(self, ratio_id):
        with self.connection:
            self.cursor.execute(
                'UPDATE ratio set ratio_dislike_value =ratio_dislike_value+ 1 where ratio_id=' + str(ratio_id))

    def update_ratio_dislike_off(self, ratio_id):
        with self.connection:
            self.cursor.execute(
                'UPDATE ratio set ratio_dislike_value =ratio_dislike_value- 1 where ratio_id=' + str(ratio_id))

    def update_ratio_to_like(self, ratio_id, user_id):
        with self.connection:
            self.cursor.execute(
                'INSERT INTO ratio_like (user_id, ratio_id) VALUES (''\'' + str(user_id) + '\',\'' + str(
                    ratio_id) + '\''')')

    def update_ratio_to_like_off(self, ratio_id, user_id):
        with self.connection:
            self.cursor.execute(
                'DELETE from ratio_like WHERE user_id=''\'' + str(user_id) + '\' AND  ratio_id= ' + str(
                    ratio_id))

    def update_ratio_to_dislike(self, ratio_id, user_id):
        with self.connection:
            self.cursor.execute(
                'INSERT INTO ratio_dislike (user_id, ratio_id) VALUES (''\'' + str(user_id) + '\',\'' + str(
                    ratio_id) + '\''')')

    def update_ratio_to_dislike_off(self, ratio_id, user_id):
        with self.connection:
            self.cursor.execute(
                'DELETE from ratio_dislike WHERE user_id=''\'' + str(user_id) + '\' AND  ratio_id= ' + str(
                    ratio_id))

    def select_ratio_value(self, ratio_id):
        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT ratio_value from ratio where ratio_id=' + str(ratio_id)).fetchall()

        for value in ratio_value:
            for ratio_value in value:
                ratio_value = ratio_value
        return ratio_value

        return ratio_value

    def select_ratio_dislike_value(self, ratio_id):
        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT ratio_dislike_value from ratio where ratio_id=' + str(ratio_id)).fetchall()

        for value in ratio_value:
            for ratio_value in value:
                ratio_value = ratio_value
        return ratio_value

        return ratio_value

    def select_ratio_to_like_to_user(self, ratio_id, user_id):

        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT ratio_like_id from ratio_like where ratio_id=' + str(ratio_id) + ' and user_id=' '\'' + str(
                    user_id) + '\'').fetchall()
        if ratio_value == []:

            return False
        else:
            return True

    def select_ratio_to_dislike_to_user(self, ratio_id, user_id):

        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT ratio_dislike_id from ratio_dislike where ratio_id=' + str(
                    ratio_id) + ' and user_id=' '\'' + str(user_id) + '\'').fetchall()
        if ratio_value == []:

            return False
        else:
            return True

    def ratio_rating_7days(self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT  * FROM ratio WHERE chat_id = ' + str(
                    chat_id) + ' AND create_time > (SELECT DATETIME(\'now\', \'-7 day\')) AND ratio_value=(SELECT MAX(ratio_value) FROM ratio WHERE  chat_id = ' + str(
                    chat_id) + ' AND create_time > (SELECT DATETIME(\'now\', \'-7 day\'))) ').fetchall()
        for value in ratio_value:
            ratio_value = value
        return ratio_value

        return ratio_value

    def ratio_rating_3_7days(self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT * FROM ratio WHERE chat_id = ' + str(
                    chat_id) + ' AND  create_time > (SELECT DATETIME(\'now\', \'-7 day\'))  ORDER BY ratio_value DESC LIMIT 3').fetchall()

        return ratio_value

    def ratio_rating_all_time(self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT * FROM ratio WHERE chat_id = ' + str(
                    chat_id) + '  ORDER BY ratio_value DESC LIMIT 3').fetchall()

        return ratio_value

    def anti_ratio_rating_all_time (self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT * FROM ratio WHERE chat_id = '+ str(chat_id) +'  ORDER BY ratio_dislike_value DESC LIMIT 3').fetchall()

        return ratio_value
    def ratio_rating_all_time_for_top(self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT * FROM ratio WHERE chat_id = ' + str(
                    chat_id) + '  ORDER BY ratio_value DESC LIMIT 1').fetchall()

        return ratio_value

    def ratio_rating_3_30days(self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT * FROM ratio WHERE chat_id = ' + str(
                    chat_id) + ' AND  create_time > (SELECT DATETIME(\'now\', \'-30 day\'))  ORDER BY ratio_value DESC LIMIT 3').fetchall()

        return ratio_value

    def ratio_rating_30days(self, chat_id):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT  * FROM ratio WHERE chat_id = ' + str(
                    chat_id) + ' AND  create_time > (SELECT DATETIME(\'now\', \'-30 day\')) AND ratio_value=(SELECT MAX(ratio_value) FROM ratio WHERE chat_id = ' + str(
                    chat_id) + ' AND  create_time > (SELECT DATETIME(\'now\', \'-30 day\'))) ').fetchall()

        for value in ratio_value:
            ratio_value = value
        return ratio_value

        return ratio_value

    def select_hash_images(self, chat_id):
        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT hash_images from hash_image where chat_id=' + str(chat_id)).fetchall()

        rows = []
        for item in ratio_value:
            for y in item:
                rows.append(y)
        return rows

    def select_file_id(self, hash_images):

        fetchall_file_id = self.cursor.execute(
            'SELECT file_id from hash_image where hash_images=' + '\'' + str(hash_images) + '\'').fetchall()
        for value in fetchall_file_id:
            for _value in value:
                file_id = _value
            break

        return file_id

    def insert_hash_image(self, hash_images, file_id, chat_id):

        with self.connection:

            self.cursor.execute(
                'INSERT INTO hash_image (hash_images, file_id, chat_id) VALUES (''\'' + str(
                    hash_images) + '\',\'' + str(
                    file_id) + '\',\'' +
                str(
                    chat_id) + '\''')')

        ratio_id = self.cursor.execute('SELECT last_insert_rowid()').fetchall()

        for ratio in ratio_id:
            for ratio_id in ratio:
                ratio_id = ratio_id
        return ratio_id

        return ratio_id

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()
