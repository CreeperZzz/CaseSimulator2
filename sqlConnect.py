#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector


def __init__() -> 'cursor':
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        passwd = 'admin',
        auth_plugin='mysql_native_password',
        database = 'case_db'
    )

    mycursor = mydb.cursor()

    # return mycursor

# mycursor.execute('SELECT user_id FROM users')
#
# for i in mycursor.fetchone():
#     print(i)


# mydb.close()