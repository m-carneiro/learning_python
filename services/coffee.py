from flask_restful import Resource, reqparse

from models.coffee import CoffeeModel

coffees = [
    {
        'coffe_id': 1,
        'type': 'arabico'
    },
    {
        'coffe_id': 2,
        'type': 'capuccino'
    },
    {
        'coffe_id': 3,
        'type': 'torrado'
    },
    {
        'coffe_id': 4,
        'type': 'preto'
    },
    {
        'coffe_id': 5,
        'type': 'com creme'
    },
    {
        'coffe_id': 6,
        'type': 'gelado'
    }
]


class Coffees(Resource):
    def get(self):
        return {'coffees': [coffee.json() for coffee in CoffeeModel.query.all()]}


class Coffee(Resource):
    request_body = reqparse.RequestParser()
    request_body.add_argument('type')

    def get(self, coffee_id):
        coffee = CoffeeModel.find_coffee(coffee_id)
        if coffee:
            return coffee.json(), 200
        return {'message': 'Coffee not found'}, 404

    def post(self, coffee_id):
        if CoffeeModel.find_by_id(coffee_id):
            return {'message': 'Coffee id "{}" already exists.'.format(coffee_id)}, 400

        request = Coffee.request_body.parse_args()
        new_coffee = CoffeeModel(coffee_id, **request)

        try:
            new_coffee.save()
        except:
            return {'message': 'An internal error occurred trying to save coffee.'}, 500

        return new_coffee.json(), 200

    def put(self, coffee_id):
        request = Coffee.request_body.parse_args()
        found_coffee = CoffeeModel.find_coffee(coffee_id)

        if found_coffee:
            found_coffee.update_coffee(**request)
            found_coffee.save()

            return found_coffee.json(), 200

        coffee = CoffeeModel(coffee_id, **request)

        try:
            coffee.save()
        except:
            return {'message': 'An internal error occurred trying to save coffee.'}, 500

        return coffee.json(), 201

    def delete(self, coffee_id):
        coffee = CoffeeModel.find_coffee(coffee_id)
        if coffee:
            try:
                coffee.delete()
            except:
                return {'message': 'An internal error occurred trying to delete coffee.'}, 500
            return {'message': 'Coffee deleted :('}
        return {'message': 'Coffee not found'}, 404
