import sqlite3
from flask_restful import Resource, reqparse
from Models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True, type=str, help='This field cannot left blank!')
    parser.add_argument('password', required=True, type=str, help='This field cannot left blank!')
    

    def post(self):
        data = UserRegister.parser.parse_args()
        user = UserModel.find_by_username(data['username'])
        if user:
            return {'message':'A user with that name already exists'}, 400
        user = UserModel(**data)    
        user.save_to_db()
        return {'message': 'user are created'}, 201
