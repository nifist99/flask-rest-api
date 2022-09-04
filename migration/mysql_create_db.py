import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        # Create a new record
        cursor.execute('CREATE DATABASE flask')

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()