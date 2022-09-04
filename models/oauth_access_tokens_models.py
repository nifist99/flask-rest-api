import pymysql.cursors
from migration.mysql_connection import con

con_mysql = con.connection()

class token:
    def index():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    oauth_access_tokens='CREATE TABLE oauth_access_tokens(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id INT NOT NULL,name VARCHAR(250),scopes VARCHAR(250),revoked INT(11),created_at DATETIME,updated_at DATETIME,expires_at DATETIME)'
                    cursor.execute(oauth_access_tokens)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def detail():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    oauth_access_tokens='CREATE TABLE oauth_access_tokens(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id INT NOT NULL,name VARCHAR(250),scopes VARCHAR(250),revoked INT(11),created_at DATETIME,updated_at DATETIME,expires_at DATETIME)'
                    cursor.execute(oauth_access_tokens)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def store():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    oauth_access_tokens='CREATE TABLE oauth_access_tokens(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id INT NOT NULL,name VARCHAR(250),scopes VARCHAR(250),revoked INT(11),created_at DATETIME,updated_at DATETIME,expires_at DATETIME)'
                    cursor.execute(oauth_access_tokens)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False

    def update():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    oauth_access_tokens='CREATE TABLE oauth_access_tokens(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id INT NOT NULL,name VARCHAR(250),scopes VARCHAR(250),revoked INT(11),created_at DATETIME,updated_at DATETIME,expires_at DATETIME)'
                    cursor.execute(oauth_access_tokens)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False
    
    def delete():
        with con_mysql:
            with con_mysql.cursor() as cursor:
                try:
                    oauth_access_tokens='CREATE TABLE oauth_access_tokens(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id INT NOT NULL,name VARCHAR(250),scopes VARCHAR(250),revoked INT(11),created_at DATETIME,updated_at DATETIME,expires_at DATETIME)'
                    cursor.execute(oauth_access_tokens)
                    con_mysql.commit()

                    return True
                except pymysql.Error as err:
                    con_mysql.rollback()
                    return False