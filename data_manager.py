import os
import requests
from flask import session
from models import db, User, Movie
from sqlalchemy import select, or_, and_
from dotenv import load_dotenv

load_dotenv()
OMDB_KEY = os.getenv('OMDB_API_KEY')

class DataManager():
    def get_users(self):
        all_users_query = (
            select(User)
            .order_by(User.name)
        )
        list_of_all_users = db.session.execute(all_users_query).scalars().all()
        return list_of_all_users

    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()

    def get_movies(self):
        all_movies_query = (
            select(Movie)
            .order_by(Movie.title)
        )
        list_of_all_movies = db.session.execute(all_movies_query).scalars().all()
        return list_of_all_movies

    def add_movie(self, title, user_id):
        url = f'http://www.omdbapi.com/?apikey={OMDB_KEY}&t={title}'
        result = requests.get(url).json()

        new_movie = Movie(
            title=title,
            director=result["Director"],
            year=result["Year"],
            poster_url=result["Poster"],
            user_id=user_id
        )

        db.session.add(new_movie)
        db.session.commit()

    def update_movie(self, movie_id, new_title):
        movie_to_update_query = (
            select(Movie)
            .where(Movie.id == movie_id)
        )

        movie_to_update = (
            db.session.execute(movie_to_update_query).scalars().one()
        )

        movie_to_update.title = new_title
        db.session.commit()

    def delete_movie(self, movie_id):
        movie_to_delete_query = (
            select(Movie)
            .where(Movie.id == movie_id)
        )
        movie_to_delete = (
            db.session.execute(movie_to_delete_query).scalars().one()
        )

        db.session.delete(movie_to_delete)
        db.session.commit()

