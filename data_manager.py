"""
Data management layer for Watchlist application.

This module handles all database operations and OMDB API integration
with comprehensive error handling and authorization checks.
"""

import os
import requests
from requests.exceptions import RequestException, ConnectionError, Timeout
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from dotenv import load_dotenv

from models import db, User, Movie


# Load environment variables and validate API key
load_dotenv()
OMDB_KEY = os.getenv('OMDB_API_KEY')
if not OMDB_KEY:
    raise EnvironmentError("OMDB_API_KEY not found in .env file")


class DataManager:
    """
    Data manager class handling all database operations and OMDB API calls.

    This class provides methods for managing users and movies with built-in
    error handling, validation, and authorization checks.
    """

    def get_users(self):
        """
        Retrieve all users ordered by name.

        Returns:
            list[User]: List of all User objects sorted alphabetically by name
        """
        all_users_query = (
            select(User)
            .order_by(User.name)
        )
        list_of_all_users = db.session.execute(all_users_query).scalars().all()
        return list_of_all_users

    def create_user(self, name):
        """
        Create a new user in the database.

        Args:
            name (str): Name of the new user
        """
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_movies(self, user_id):
        """
        Retrieve all movies for a specific user ordered by title.

        Args:
            user_id (int): User ID to fetch movies for

        Returns:
            list[Movie]: List of Movie objects for the specified user
        """
        all_movies_query = (
            select(Movie)
            .where(user_id == Movie.user_id)
            .order_by(Movie.title)
        )
        list_of_all_movies = db.session.execute(all_movies_query).scalars().all()
        return list_of_all_movies

    def add_movie(self, title, user_id):
        """
        Add a new movie to user's watchlist via OMDB API.

        Fetches movie data from OMDB API, validates the data, and creates
        a new movie entry with authorization check.

        Args:
            title (str): Movie title to search for
            user_id (int): User ID to add movie to

        Returns:
            tuple: (success: bool, error_message: str or None)
                - (True, None) on success
                - (False, error_message) on failure
        """
        # Verify user exists
        user_exists = db.session.query(db.exists().where(User.id == user_id)).scalar()
        if not user_exists:
            return False, "User not found."

        url = f'http://www.omdbapi.com/?apikey={OMDB_KEY}&t={title}'

        try:
            # Fetch movie data from OMDB API
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            result = response.json()

            # Check if OMDB found the movie
            if result['Response'] == 'False':
                error = result['Error']
                return False, error

            # Validate required fields
            if 'Director' not in result or 'Year' not in result:
                return False, 'Incomplete movie data from OMDb!'

            # Extract and process movie data
            director = result['Director']
            year_str = result['Year']
            try:
                year = int(year_str.split('-')[0])
            except (ValueError, AttributeError):
                year = 0

            poster_url = result['Poster']
            if poster_url == 'N/A':
                poster_url = None

            # Create and save movie
            new_movie = Movie(
                title=title,
                director=director,
                year=year,
                poster_url=poster_url,
                user_id=user_id
            )

            db.session.add(new_movie)
            db.session.commit()
            return True, None

        except Timeout:
            return False, 'Request timed out!'
        except ConnectionError:
            return False, 'Connection error!'
        except RequestException as e:
            return False, f'API-Error: {str(e)}'
        except ValueError:
            return False, 'Invalid data from OMDb'
        except Exception as e:
            db.session.rollback()
            return False, f'An error occured: {str(e)}'

    def update_movie(self, movie_id, user_id, new_title):
        """
        Update movie title with authorization check.

        Verifies that the movie belongs to the specified user before
        allowing the update operation.

        Args:
            movie_id (int): Movie ID to update
            user_id (int): User ID requesting the update
            new_title (str): New movie title

        Returns:
            tuple: (success: bool, error_message: str or None)
                - (True, None) on success
                - (False, error_message) on failure (not found, permission denied, etc.)
        """
        if not new_title or not new_title.strip():
            return False, "Movie title cannot be empty"

        try:
            # Get movie
            movie_to_update_query = select(Movie).where(Movie.id == movie_id)
            movie_to_update = db.session.execute(movie_to_update_query).scalars().one()

            # Ownership Check
            if movie_to_update.user_id != user_id:
                return False, "You do not have permission to update this movie"

            # Update
            movie_to_update.title = new_title.strip()
            db.session.commit()
            return True, None

        except NoResultFound:
            return False, "Movie not found"
        except Exception as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"

    def delete_movie(self, movie_id, user_id):
        """
        Delete movie with authorization check.

        Verifies that the movie belongs to the specified user before
        allowing the delete operation.

        Args:
            movie_id (int): Movie ID to delete
            user_id (int): User ID requesting the deletion

        Returns:
            tuple: (success: bool, error_message: str or None)
                - (True, None) on success
                - (False, error_message) on failure (not found, permission denied, etc.)
        """
        try:
            # Get movie
            movie_to_delete_query = select(Movie).where(Movie.id == movie_id)
            movie_to_delete = db.session.execute(movie_to_delete_query).scalars().one()

            # Ownership Check
            if movie_to_delete.user_id != user_id:
                return False, "You do not have permission to delete this movie"

            # Delete
            db.session.delete(movie_to_delete)
            db.session.commit()
            return True, None

        except NoResultFound:
            return False, "Movie not found"
        except Exception as e:
            db.session.rollback()
            return False, f"Database error: {str(e)}"
