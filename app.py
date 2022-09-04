from config.config import config

from multiprocessing.sharedctypes import Value
from flask import Flask, render_template , url_for, redirect, request, session, flash

app = Flask(__name__)

if __name__ == "__main__":
    app.config.from_object('config.prod')