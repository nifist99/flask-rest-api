import pymysql.cursors
from migration.mysql_connection import con

con_mysql = con.connection()

class users:
    def index():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    users='CREATE TABLE users(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    users+='name VARCHAR(20),'
                    users+='email VARCHAR(250) NOT NULL,'
                    users+='password VARCHAR(1000) NOT NULL,'
                    users+='status VARCHAR(250) NOT NULL,'
                    users+='email_verified_at DATE,'
                    users+='remember_token VARCHAR(1000),'
                    users+='created_at DATETIME,'
                    users+='updated_at DATETIME'
                    users+=')'

                    cursor.execute(users)

                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def detail():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    users='CREATE TABLE users(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    users+='name VARCHAR(20),'
                    users+='email VARCHAR(250) NOT NULL,'
                    users+='password VARCHAR(1000) NOT NULL,'
                    users+='status VARCHAR(250) NOT NULL,'
                    users+='email_verified_at DATE,'
                    users+='remember_token VARCHAR(1000),'
                    users+='created_at DATETIME,'
                    users+='updated_at DATETIME'
                    users+=')'

                    cursor.execute(users)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def store():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    users='CREATE TABLE users(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    users+='name VARCHAR(20),'
                    users+='email VARCHAR(250) NOT NULL,'
                    users+='password VARCHAR(1000) NOT NULL,'
                    users+='status VARCHAR(250) NOT NULL,'
                    users+='email_verified_at DATE,'
                    users+='remember_token VARCHAR(1000),'
                    users+='created_at DATETIME,'
                    users+='updated_at DATETIME'
                    users+=')'

                    cursor.execute(users)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def update():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    users='CREATE TABLE users(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    users+='name VARCHAR(20),'
                    users+='email VARCHAR(250) NOT NULL,'
                    users+='password VARCHAR(1000) NOT NULL,'
                    users+='status VARCHAR(250) NOT NULL,'
                    users+='email_verified_at DATE,'
                    users+='remember_token VARCHAR(1000),'
                    users+='created_at DATETIME,'
                    users+='updated_at DATETIME'
                    users+=')'

                    cursor.execute(users)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False
    
    def delete():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    users='CREATE TABLE users(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                    users+='name VARCHAR(20),'
                    users+='email VARCHAR(250) NOT NULL,'
                    users+='password VARCHAR(1000) NOT NULL,'
                    users+='status VARCHAR(250) NOT NULL,'
                    users+='email_verified_at DATE,'
                    users+='remember_token VARCHAR(1000),'
                    users+='created_at DATETIME,'
                    users+='updated_at DATETIME'
                    users+=')'

                    cursor.execute(users)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False