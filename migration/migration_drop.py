import pymysql.cursors
from mysql_connection import con

con_mysql = con.connection()

with con_mysql:
    with con_mysql.cursor() as cursor:
        # Create a new table
        try:
            employee='DROP TABLE employee'
            cursor.execute(employee)
            print("drop table successfully employee")
        except pymysql.Error as err:
            print(err)
            pass
        finally:
            pass

        try:
            users='DROP TABLE users'
            cursor.execute(users)
            print("drop table successfully users")
        except pymysql.Error as err:
            print(err)
            pass
        finally:
            pass

    con_mysql.commit()