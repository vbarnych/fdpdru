from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime as dt

DB_URL = 'postgresql+psycopg2://test_user:password@127.0.0.1:5432/test_db'
from core import db
from models import Actor, Movie


app = Flask(__name__, instance_relative_config=False)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # silence the deprecation warning

db.init_app(app)

data = {'name' : 'Megan Fox', 'gender' : 'female', 'date_of_birth' : dt.strptime('16.05.1986', '%d.%m.%Y').date()}

with app.app_context():

    db.create_all()       # помилка під час виконання цього рядка
    obj = Actor(**data)
    db.session.add(obj)
    db.session.commit()
    db.session.refresh(obj)
    print(obj)
    print(obj.__dict__)