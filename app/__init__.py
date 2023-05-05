"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa68ik728r88627k10-a.oregon-postgres.render.com",
        database="todo_hyx3",
        user="root",
        password="7VVD4MJi0zdDQE64uQCKiFZXdO3hzmh4")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
