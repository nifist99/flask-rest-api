import pymysql.cursors
from migration.mysql_connection import con

con_mysql = con.connection()

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
                    
                    data = cursor.fetchone()

                    return data
                except pymysql.Error as err:
                    error = err
                    pass
                finally:
                    con_mysql.close()
                    return error

    def store(name, email, password):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users="INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                    value=(name,email,password)

                    cursor.execute(users,value)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def update(id,name,email):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users='UPDATE users SET name = %s,email = %s WHERE id = %s'
                    value =(name,email,id)
                    cursor.execute(users,value)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False
    
    def delete(id):
                try:
                    conn = con.connection()
                    cursor =conn.cursor()
                    users='DELETE FROM users WHERE id = %s'
                    cursor.execute(users,id)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False