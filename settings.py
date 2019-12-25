from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from req import Users, Users1, Users2, \
    Users3, Messages, Messages2, Rooms, \
    Rooms2


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///big_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

api.add_resource(Users, '/users')
api.add_resource(Users1, '/users/<int:user_id>')
api.add_resource(Messages, '/messages')
api.add_resource(Users2, '/users/<int:user_id>/messages')
api.add_resource(Messages2, '/rooms/<int:room_id>/messages')
api.add_resource(Users3, '/rooms/<int:room_id>/users')
api.add_resource(Rooms, '/rooms')
api.add_resource(Rooms2, '/rooms/<int:room_id>')

if __name__ == '__main__':
    app.run(port=6002, debug=True)
