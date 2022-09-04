from config.config import config
from multiprocessing.sharedctypes import Value
from flask import Flask, render_template , url_for, redirect, request, session, flash
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)