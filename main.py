"""Here We are Practising the DataBase Execution
    using pymysql"""
import errno

import mysql.connector
from mysql.connector import errorcode


class DataBase:
    @staticmethod
    def connection_database():
        try:
            conn = mysql.connector.connect(host='losthost', user='root', port='2003', password='',
                                           database='28december2021')
            cursor = conn.cursor()
        except mysql.connector.Error as er:
            if er.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something Wrong with Username and password")
            elif er.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doe not exist")
            else:
                print(er)

