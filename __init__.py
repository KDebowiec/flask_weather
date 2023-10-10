from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
api_key = 'f0b9b53e325744edae5140611230610'
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    db.init_app(app)
    app.debug = True

    from .main import

    with app.app_context():
        db.create_all()
    return app
