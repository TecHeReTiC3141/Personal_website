import sqlite3

class DataBase:

    def __init__(self, conn: sqlite3.Connection):
        self.__conn = conn
        self.__curs = self.__conn.cursor()
