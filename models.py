from flask_sqlalchemy import SQLalchemy

db = SQLalchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'User(id: {type(self.id)}:{self.id}, name: {type(self.name)}:{self.name})'

    def __str__(self):
        return self.name

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'Movie(id: {type(self.id)}:{self.id}, title: {type(self.title)}:{self.title})'

    def __str__(self):
        return self.title

