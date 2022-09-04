import pymysql.cursors
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

# Connect to the database

class con:
    def connection():
        connection = pymysql.connect(host=os.getenv('DB_HOST'),
                                    user=os.getenv('DB_USERNAME'),
                                    password=os.getenv('DB_PASSWORD'),
                                    database=os.getenv('DB_DATABASE'),
                                    cursorclass=pymysql.cursors.DictCursor)

        return connection