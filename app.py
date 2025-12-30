"""
Flask web application for managing movie watchlists.

This application provides routes for user and movie management with OMDB API integration.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import select, or_, and_

from data_manager import DataManager
from models import db, Movie, User


# Flask Application Setup
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/watchlist.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
data_manager = DataManager()


# User Routes
@app.route('/')
def list_users():
    """
    Display homepage with list of all users.

    Returns:
        Rendered home.html template with users list and success flag
    """
    users = data_manager.get_users()
    is_success = request.args.get('success') is not None
    return render_template('home.html', users=users, success=is_success)


@app.route('/users', methods=['POST'])
def create_a_new_user():
    """
    Create a new user from form data.

    Returns:
        Redirect to homepage with success status
    """
    username = request.form.get('username')
    if username:
        data_manager.create_user(username)
        is_success = True
    else:
        is_success = False
    return redirect(url_for('list_users', success=is_success))


# Movie Routes
@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_favorite_movies(user_id):
    """
    Display a user's movie watchlist.

    Args:
        user_id (int): User ID from URL

    Returns:
        Rendered movies.html template with movies and status flags
    """
    favorite_movies = data_manager.get_movies(user_id)
    is_success = request.args.get('success') is not None
    is_error = request.args.get('error') is not None
    is_update = request.args.get('update') is not None
    is_deleted = request.args.get('delete') is not None
    return render_template('movies.html', user_id=user_id, movies=favorite_movies,
                          success=is_success, error=is_error, update=is_update, delete=is_deleted)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_favorite_movie(user_id):
    """
    Add a new movie to user's watchlist via OMDB API.

    Args:
        user_id (int): User ID from URL

    Returns:
        Redirect to movies page with success or error message
    """
    movie = request.form.get('movie')
    if movie:
        success, error_message = data_manager.add_movie(movie, user_id)
        if success:
            return redirect(url_for('get_favorite_movies', user_id=user_id, success=True))
        else:
            return redirect(url_for('get_favorite_movies', user_id=user_id, error=error_message))
    else:
        return redirect(url_for('get_favorite_movies', user_id=user_id, error="Movie title required"))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_favorite_movie(user_id, movie_id):
    """
    Update a movie's title with authorization check.

    Args:
        user_id (int): User ID from URL
        movie_id (int): Movie ID from URL

    Returns:
        Redirect to movies page with success or error message
    """
    new_title = request.form.get('movie-title')

    if not new_title:
        return redirect(url_for('get_favorite_movies', user_id=user_id, error="Movie title required"))

    success, error_message = data_manager.update_movie(movie_id, user_id, new_title)

    if success:
        return redirect(url_for('get_favorite_movies', user_id=user_id, update=True))
    else:
        return redirect(url_for('get_favorite_movies', user_id=user_id, error=error_message))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_favorite_movie(user_id, movie_id):
    """
    Delete a movie from watchlist with authorization check.

    Args:
        user_id (int): User ID from URL
        movie_id (int): Movie ID from URL

    Returns:
        Redirect to movies page with success or error message
    """
    success, error_message = data_manager.delete_movie(movie_id, user_id)

    if success:
        return redirect(url_for('get_favorite_movies', user_id=user_id, delete=True))
    else:
        return redirect(url_for('get_favorite_movies', user_id=user_id, error=error_message))


# Error Handlers
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found errors.

    Args:
        error: The error object

    Returns:
        Rendered 404.html template with 404 status code
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 Internal Server errors.

    Args:
        error: The error object

    Returns:
        Rendered 500.html template with 500 status code
    """
    db.session.rollback()  # Rollback failed transactions
    return render_template('500.html'), 500


# Application Entry Point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print(f' * Datenbank initialisiert.')
    app.run('0.0.0.0', 5002, debug=True)
