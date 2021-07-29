# -*- coding: utf-8 -*-
import sqlite3
import sys
from datetime import datetime





class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def creator_photo_ratio(self, message, photo_id, user_id, message_id):

        with self.connection:

            self.cursor.execute(
                'INSERT INTO ratio (photo_id, user_id, create_time, message_id) VALUES (''\'' + str(photo_id) + '\',\'' + str(
                    user_id) + '\',\'' +
                str(
                    datetime.utcfromtimestamp(message.date).strftime('%Y-%m-%d %H:%M:%S')) + '\',\'' + str(message_id) + '\''')')

        ratio_id = self.cursor.execute('SELECT last_insert_rowid()').fetchall()

        for ratio in ratio_id:
            for ratio_id in ratio:
                ratio_id = ratio_id
        return ratio_id

        return ratio_id

    def update_ratio_like(self, ratio_id ):
        with self.connection:
            self.cursor.execute(
                'UPDATE ratio set ratio_value =ratio_value+ 1 where ratio_id=' + str(ratio_id))

    def update_ratio_to_like(self, ratio_id, user_id):
        with self.connection:
            self.cursor.execute(
                'INSERT INTO ratio_like (user_id, ratio_id) VALUES (''\'' + str(user_id) + '\',\'' + str(
                    ratio_id) + '\''')')

    def update_ratio_dislike(self, ratio_id):
        with self.connection:
            self.cursor.execute(
                'UPDATE ratio set ratio_value =ratio_value- 1 where ratio_id=' + str(ratio_id))

    def select_ratio_value(self, ratio_id):
        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT ratio_value from ratio where ratio_id=' + str(ratio_id)).fetchall()

        for value in ratio_value:
            for ratio_value in value:
                ratio_value = ratio_value
        return ratio_value

        return ratio_value

    def select_ratio_to_like_to_user(self, ratio_id, user_id):


        with self.connection:

            ratio_value = self.cursor.execute(
                'SELECT ratio_like_id from ratio_like where ratio_id=' + str(ratio_id) + ' and user_id=' '\'' +str(user_id)+'\'').fetchall()
        if ratio_value == []:

            return False
        else:
            return True


    def ratio_rating_7days(self):


        with self.connection:


            ratio_value = self.cursor.execute(
                'SELECT  * FROM ratio WHERE create_time > (SELECT DATETIME(\'now\', \'-7 day\')) AND ratio_value=(SELECT MAX(ratio_value) FROM ratio WHERE create_time > (SELECT DATETIME(\'now\', \'-7 day\'))) ').fetchall()
        for value in ratio_value:

             ratio_value=value
        return ratio_value

        return ratio_value

    def ratio_rating_30days(self):

        with self.connection:
            ratio_value = self.cursor.execute(
                'SELECT  * FROM ratio WHERE create_time > (SELECT DATETIME(\'now\', \'-30 day\')) AND ratio_value=(SELECT MAX(ratio_value) FROM ratio WHERE create_time > (SELECT DATETIME(\'now\', \'-30 day\'))) ').fetchall()

        for value in ratio_value:
            ratio_value = value
        return ratio_value

        return ratio_value

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()