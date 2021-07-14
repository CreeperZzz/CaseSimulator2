#!/usr/bin/python
# -*- coding: UTF-8 -*-

import mysql.connector


class Sql:

    def __init__(self) -> 'cursor':
        mydb = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'admin',
            auth_plugin='mysql_native_password',
            database = 'case_db'
        )

        self.connection = mydb

        # return mycursor #.execute(f'SELECT * FROM rate WHERE cid = 0')

    def get_rate(self, cid: int = 0) -> 'list':
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT e,d,c,b,a,s,g FROM rate WHERE cid = {cid}')
        return cursor.fetchone()

    def get_case_list(self) -> 'list':
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT cid,cname FROM case_db.case')
        return cursor.fetchall()

    def get_case_name(self, cid: int = 0) -> 'list':
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT cname FROM case_db.case WHERE cid = {cid}')
        return cursor.fetchone()

    def get_num_of_weaps(self, cid: int = 0) -> int:
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT num_of_weaps FROM case_db.case WHERE cid = {cid}')
        return cursor.fetchone()

    def get_weaplist(self, cid: int = 0) -> 'list':
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT tname, wname FROM weapon w,type t WHERE cid = {cid} and w.tid = t.tid;')
        return cursor.fetchall()

    def get_weaplist_qua(self, qid: int, cid: int = 0) -> 'list':
        cursor = self.connection.cursor()
        cursor.execute(f'SELECT tname, wname FROM weapon w,type t WHERE cid = {cid} and qid = {qid} and w.tid = t.tid;')
        return cursor.fetchall()

    def close(self):
        self.connection.close();
# mycursor.execute('SELECT user_id FROM users')
#
# for i in mycursor.fetchone():
#     print(i)


# mydb.close()