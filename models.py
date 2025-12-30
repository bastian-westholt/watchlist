"""
Database models for Watchlist application.

This module defines the SQLAlchemy ORM models for users and movies.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """
    User model representing a watchlist user.

    Attributes:
        id (int): Primary key, auto-incremented user ID
        name (str): User's name (max 100 characters)
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Developer-friendly string representation."""
        return f'User(id: {self.id}, name: {self.name})'

    def __str__(self):
        """User-friendly string representation."""
        return self.name


class Movie(db.Model):
    """
    Movie model representing a movie in a user's watchlist.

    Attributes:
        id (int): Primary key, auto-incremented movie ID
        title (str): Movie title (max 100 characters)
        director (str): Director name (max 100 characters)
        year (int): Release year
        poster_url (str): URL to movie poster image (optional, max 200 characters)
        user_id (int): Foreign key referencing User.id
    """
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    poster_url = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        """Developer-friendly string representation."""
        return f'Movie(id: {self.id}, title: {self.title})'

    def __str__(self):
        """User-friendly string representation."""
        return self.title
