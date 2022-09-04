import pymysql.cursors
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# Connect to the database
connection = pymysql.connect(host=os.getenv('DB_HOST'),
                                    user=os.getenv('DB_USERNAME'),
                                    password=os.getenv('DB_PASSWORD'),
                                    database=os.getenv('DB_DATABASE'),
                                    cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
        # Create a new record
        cursor.execute('CREATE DATABASE flask')

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()