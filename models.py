import datetime
from sqlalchemy.orm import relationship
from settings import db

mem = db.Table(
    'mem',
    db.Column('room_id', db.Integer, db.ForeignKey('room.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

mes = db.Table(
    'mes',
    db.Column('room_id', db.Integer, db.ForeignKey('room.id')),
    db.Column('message_id', db.Integer, db.ForeignKey('message.id'))
)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    country = db.Column(db.String(80), unique=True, nullable=False)
    avatar = db.Column(db.String(80), unique=True, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

    def __repr__(self):
        return '<User %r>' % self.name


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = relationship('User', foreign_keys=[sender_id])
    receiver = relationship('User', foreign_keys=[receiver_id])

    def serialize(self):
        return {
            'id': self.id,
            'sender': self.sender_id,
            'receiver': self.receiver_id,
            'text': self.text
        }

    def __repr__(self):
        return '<Message %r>' % self.text


class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    members = db.relationship(
        'User', secondary=mem, backref=db.backref('members', lazy='dynamic'
                                                  )
    )
    messages = db.relationship(
        'Message', secondary=mes, backref=db.backref('messages', lazy='dynamic'
                                                     )
    )


if __name__ == '__main__':
    db.create_all()
