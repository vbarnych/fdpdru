from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime as dt


from sqlalchemy import engine,exc


try:
    #DB_URL = 'postgresql+psycopg2://test_user:password@127.0.0.1:5432/test_db'   #os.environ['DB_URL']  
    DB_URL = os.environ['DB_URL']  
#postgresql+psycopg2://test_user:password@0.0.0.0:5432/test_db

#patch_all()

    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    
    #db.init_app(app)   
    db = SQLAlchemy(app)

except exc.SQLAlchemyError as e:
        print(str(e))



#db = SQLAlchemy()


def create_app():
    '''"""Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
    
    #db.init_app(app)   
    db = SQLAlchemy(app)'''


    with app.app_context():
        # Imports
        from . import routes
        print("data base :")
        print(db)
        # Create tables for our models
        #db.create_all()       # помилка під час виконання цього рядка

        return app
        


