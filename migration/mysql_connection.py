import pymysql.cursors

# Connect to the database

class con:
    def connection():
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    database='flask',
                                    cursorclass=pymysql.cursors.DictCursor)

        return connection