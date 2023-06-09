from flask_restful import Resource, reqparse

from models.user import UserModel


class User(Resource):

    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return {'message': 'User not found'}, 404

    def post(self, user_id):
        if UserModel.find_user(user_id):
            return {'message': f'User {user_id} already exists'}, 400

        data = User.parser.parse_args()
        user = UserModel(user_id, **data)
        user.save_user()
        return user.json()

    def put(self, user_id):
        data = User.parser.parse_args()
        user = UserModel.find_user(user_id)

        if user:
            user.update_user(**data)
            return user.json()

        user = UserModel(user_id, **data)
        user.save_user()
        return user.json()

    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': f'User {user_id} deleted'}
        return {'message': f'User {user_id} not found'}, 404


class UserRegister(Resource):
    def post(self):
        data = reqparse.RequestParser()
        data.add_argument('username', type=str, required=True, help='Username is required')
        data.add_argument('password', type=str, required=True, help='Password is required')
        data = data.parse_args()

        user = UserModel(**data)
        user.save_user()
        return user.json(), 201