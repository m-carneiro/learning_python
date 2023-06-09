from sql_alchemy import db


class CoffeeModel(db.Model):
    __tablename__ = 'coffees'

    coffee_id = db.Column(db.String, primary_key=True)
    coffee_type = db.Column(db.String(80))

    def __init__(self, coffee_id, coffee_type):
        self.coffee_id = coffee_id
        self.type = coffee_type

    def json(self):
        return {
            'coffee_id': self.coffee_id,
            'type': self.type
        }

    @classmethod
    def find_coffee(cls, coffee_id):
        coffee = cls.query.filter_by(coffee_id=coffee_id).first()
        if coffee:
            return coffee
        return None

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update_coffee(self, coffee_type):
        self.type = coffee_type
        self.save()

    def delete(self):
        db.session.delete(self)
        db.session.commit()