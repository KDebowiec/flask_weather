from __future__ import annotations
from . import db


class History(db.Model):
    __tablename__ = 'history'
    _id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), unique=False)
    temperature = db.Column(db.String(100), unique=False)
    wind = db.Column(db.String(100), unique=False)
    humidity = db.Column(db.String(100), unique=False)

    def __init__(self, city, temperature, wind, humidity):
        self.city, self.temperature, self.wind, self.humidity = city, temperature, wind, humidity
