import pymysql.cursors
from mysql_connection import con

con_mysql = con.connection()

with con_mysql:
    with con_mysql.cursor() as cursor:
        # Create a new table
        try:
            oauth_access_tokens='CREATE TABLE oauth_access_tokens(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,user_id INT NOT NULL,name VARCHAR(250),scopes VARCHAR(250),revoked INT(11),created_at DATETIME,updated_at DATETIME,expires_at DATETIME)'
            cursor.execute(oauth_access_tokens)
            print("create table successfully oauth_access_tokens")
        except pymysql.Error as err:
            print(err)
            pass
        finally:
            pass

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

            print("create table successfully users")

        except pymysql.Error as err:
            print(err)
            pass
        finally:
            pass
    con_mysql.commit()
