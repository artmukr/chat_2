from models import User, Message, Room
from settings import db


def get_all_users():
	return User.query.all()


def get_all_messages_from_room(room_id):
	return Room.query.get(room_id).messages


def get_all_rooms():
	return [r.name for r in Room.query.all()]


def get_all_users_from_room(room_id):
	return Room.query.get(room_id).members


def get_user(user_id):
	return User.query.get(user_id)


def get_users_messages(user_id, role):
	if role == 'sender_id':
		return Message.query.filter_by(sender_id=user_id).all()
	elif role == 'receiver_id':
		return Message.query.filter_by(receiver_id=user_id).all()


def get_messages_of_dialogue(sender_id, receiver_id):
	return Message.query.filter_by(
			sender_id=sender_id, receiver_id=receiver_id).all()


def create_user(data):
	new_user = User(
		name=data['name'], email=data['email'],
		country=data['country'], avatar=data['avatar'])
	db.session.add(new_user)
	db.session.commit()
	return {}


def create_room(name):
	new_room = Room(name=name)
	db.session.add(new_room)
	db.session.commit()
	return {}


def add_user_to_room(room_id, user_id):
	room = Room.query.get(room_id)
	user = User.query.get(user_id)
	room.members.append(user)
	db.session.commit()
	return {}


def send_message_to_room(room_id, sender_id, message):
	sender = User.query.get(sender_id)
	room = Room.query.get(room_id)
	mes = Message(author=sender, text=message)
	db.session.add(mes)
	room.messages.append(mes)
	db.session.commit()
	return {}


def patch_room(room_id, data):
	db.session.query(Room).get(room_id).update(data)
	db.session.commit()
	return {}


def patch_user(user_id, data):
	db.session.query(User).get(user_id).update(data)
	db.session.commit()
	return {}


def delete_room(room_id):
	mod = Room.query.get(room_id)
	db.session.delete(mod)
	db.session.commit()
	return {}


def delete_user(user_id):
	us = User.query.get(user_id)
	db.session.delete(us)
	db.session.commit()
	return {}
