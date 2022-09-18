import sqlite3

from flask import Flask
from pathlib import Path

DATABASE = 'database.db'
SECRET_KEY = 'e7463a675de3b7453990742469ba869b57086d6e'
MAX_CONTENT_SIZE = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update({'DATABASE': Path(app.root_path) / DATABASE})


def connect_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn