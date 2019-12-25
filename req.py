from flask_restful import Resource, reqparse
from flask import request, jsonify
from functions \
    import get_all_users, get_users_messages, get_all_messages_from_room, \
    get_all_rooms, get_all_users_from_room, get_user, send_message_to_room, \
    add_user_to_room, delete_room, delete_user, create_user, create_room, \
    patch_user, patch_room, get_messages_of_dialogue


class Users(Resource):
    def get(self):
        return [u.serialize() for u in get_all_users()], 200

    def post(self):
        data = request.get_json()
        return jsonify(create_user(data)), 201


class Users1(Resource):
    def get(self, user_id):
        return get_user(user_id).serialize(), 200

    def patch(self, user_id):
        data = request.get_json()
        return patch_user(user_id, data), 204

    def delete(self, user_id):
        return delete_user(user_id), 200


class Users2(Resource):
    def get(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('role', type=str)
        role = parser.parse_args()
        return get_users_messages(user_id, role), 200


class Users3(Resource):
    def get(self, room_id):
        return get_all_users_from_room(room_id), 200

    def post(self, room_id):
        req_ = request.get_json()
        user_id = req_['user_id']
        return add_user_to_room(room_id, user_id), 201


class Messages(Resource):
    def get(self):
        parser1 = reqparse.RequestParser()
        parser2 = reqparse.RequestParser()
        parser1.add_argument('sender_id', type=str)
        parser2.add_argument('receiver_id', type=str)
        sender_id = parser1.parse_args()
        receiver_id = parser2.parse_args()
        return get_messages_of_dialogue(sender_id, receiver_id), 200


class Messages2(Resource):
    def get(self, room_id):
        return get_all_messages_from_room(room_id), 200

    def post(self, room_id):
        req_ = request.get_json()
        user_id = req_['user_id']
        message = req_['message']
        return send_message_to_room(room_id, user_id, message), 201


class Rooms(Resource):
    def get(self):
        return get_all_rooms(), 200

    def post(self):
        req_ = request.get_json()
        name = req_['name']
        return create_room(name), 201


class Rooms2(Resource):
    def get(self, room_id):
        pass

    def patch(self, room_id):
        req_ = request.get_json()
        return patch_room(room_id, req_), 204

    def delete(self, room_id):
        return delete_room(room_id), 200
