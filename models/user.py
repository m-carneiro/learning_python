from sql_alchemy import db


class UserModel(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def json(self):
        return {
            'user_id': self.user_id,
            'username': self.username
        }

    @classmethod
    def find_user(cls, username):
        user = cls.query.filter_by(username=username).first()
        if user:
            return user
        return None

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def update_user(self, username, password):
        self.username = username
        self.password = password
        db.session.commit()

    def __repr__(self):
        return f'User(username={self.username})'
