import sqlite3
from time import *


class DataBase:

    def __init__(self, conn: sqlite3.Connection):
        self.__db = conn
        self.__curs = self.__db.cursor()

    def getData(self, request, data: list | tuple = (), fetch='all') -> list[dict]:
        try:
            self.__curs.execute(request, data)
            if fetch == 'all':
                res = self.__curs.fetchall()
            else:
                res = self.__curs.fetchone()
            return res
        except Exception as e:
            print(e)
        return []

    def addData(self, request, data: list | tuple = ()):
        try:
            self.__curs.execute(request, data)
            self.__db.commit()
            return 'Successfully added'
        except Exception as e:
            print(e)
            return e

    def updateData(self, request, data: list | tuple = ()):
        try:
            self.__curs.execute(request, data)
            self.__db.commit()
            return 'Successfully modified'
        except Exception as e:
            print(e)
            return e

    def add_comment(self, project_name, user_name, mark, text):
        get_id = '''SELECT id FROM projects
                    WHERE name = (?)'''
        proj_id = self.getData(get_id, (project_name,), 'one')[0]
        time_posted = round(time())
        time_format = strftime('%d.%m.%Y at %H:%M', gmtime(time_posted))
        req = '''INSERT INTO comments (project, user_name, mark, text, date)
                VALUES (?, ?, ?, ?, ?)'''

        return self.addData(req, (proj_id, user_name, mark, text, time_format))

    def get_comments(self, project_name):

        req = '''SELECT user_name, mark, text, date
                FROM projects JOIN comments ON comments.project = projects.id
                WHERE projects.name = (?)'''
        return self.getData(req, (project_name,))
