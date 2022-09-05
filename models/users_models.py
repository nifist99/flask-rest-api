import pymysql.cursors
from migration.mysql_connection import con
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from pytz import timezone
import os


date = datetime.datetime.now()

class users:
    def index():
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    
                    users='SELECT * FROM users'

                    cursor.execute(users)

                    row = cursor.fetchall()

                    conn.close()

                    data = dict()
                    data['status']  =True
                    data['message'] ='success get data'
                    data['code']    = 200
                    data['data']    = row
                    return data
                except pymysql.Error as err:
                    conn.close()
                    data = dict()
                    data['status']  =False
                    data['message'] = 'failed get data'
                    data['code']    = 401
                    data['data']    = []
                    return data

    def detail(id):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users='SELECT * FROM users WHERE id=%s',id

                    cursor.execute(users)
                    
                    row = cursor.fetchone()

                    conn.close()

                    data = dict()
                    data['status']  =True
                    data['message'] ='success get data'
                    data['code']    = 200
                    data['data']    = row

                    return data
                except pymysql.Error as err:
                    conn.close()
                    data = dict()
                    data['status']  =False
                    data['message'] = 'failed get data'
                    data['code']    = 401
                    data['data']    = []
                    return data



    def store(name, email, password):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()

                    users="INSERT INTO users (name, email, password,status,created_at) VALUES (%s, %s, %s,%s,%s)"
                    value=(name,email,generate_password_hash(password),'active',date)

                    cursor.execute(users,value)
                    conn.commit()

                    conn.close()

                    data = dict()
                    data['status']  =True
                    data['message'] ='success save data'
                    data['code']    = 200
                    return data
                except pymysql.Error as err:
                    conn.rollback()
                    print(err)
                    error = dict()
                    error['status']  =False
                    error['message'] ='failed save data'
                    error['code']    = 400
                    return error

    def update(id,name,email):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users='UPDATE users SET name = %s,email = %s WHERE id = %s'
                    value =(name,email,id)
                    cursor.execute(users,value)
                    conn.commit()

                    return True
                except pymysql.Error as err:
                    conn.rollback()
                    return False
    
    def delete(id):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users='DELETE FROM users WHERE id = %s'
                    cursor.execute(users,id)
                    conn.commit()

                    return True
                except pymysql.Error as err:
                    conn.rollback()
                    return False


    def check_email(email):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users='SELECT * FROM users WHERE email=%s'

                    cursor.execute(users,email)
                    
                    data = cursor.fetchone()

                    conn.close()

                    return data
                except pymysql.Error as err:
                    conn.close()
                    data = None
                    return data