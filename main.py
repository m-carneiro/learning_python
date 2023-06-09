from flask import Flask
from flask_restful import Api

from services.coffee import Coffee, Coffees
from services.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_request
def create_database():
    db.create_all()


api.add_resource(Coffees, '/coffees')
api.add_resource(Coffee, '/coffee/<string:id>')
api.add_resource(User, '/user/<string:username>')

if __name__ == '__main__':
    from sql_alchemy import db

    db.init_app(app)
    app.run(debug=True)
