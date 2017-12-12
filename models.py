from datetime import datetime

from app import db


class HeartBeat(db.Model):
    __tablename__ = 'HeartBeat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<HeartBeat %r>' % (self.timestamp)
