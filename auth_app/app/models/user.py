from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))

    def __repr__(self):
        return f'<Id "{self.id}", User "{self.username}", Password "{self.password}">'

