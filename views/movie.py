from flask import request
from flask_restx import Resource, Namespace

from dao.model.models_db import MovieSchema
from implemented import movie_service

movies_ns = Namespace("movies")

@movies_ns.route("/")
class MoviesView(Resource):
    """
    Класс для обработки запросов в базу.
    """
    def get(self) -> list:
        """
        Функция для вывода всех фильмов в базе.
        :return: list
        """
        schema = MovieSchema(many=True)

        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        if genre_id:
            return schema.dump(movie_service.filter_movies_by_genre(int(genre_id))), 200

        movies = schema.dump(movie_service.get_movies(request.args))
        return movies

    def post(self):
        """
        Функция для добавления фильма в базу.
        :return:
        """
        new_movie = movie_service.create_movie(request.json)
        return "", 201, {"location": f"{movies_ns.path}/{new_movie.id}"}


@movies_ns.route("/<int:movie_id>")
class MovieView(Resource):
    """
    Класс для обработки запросов в базу.
    """
    def get(self, movie_id: int):
        """
        Функция принимает значение movie_id, целое число и возращает фильм с указанным id.
        Если такого фильма нет сообщает об этом.
        :param movie_id: int
        :return: list
        """
        movie = MovieSchema().dump(movie_service.get_movies(movie_id))
        return movie

    def patch(self, movie_id: int):
        return MovieSchema().dump(movie_service.update_movie_partial(movie_id, request.json))

    def put(self, movie_id):
        """
        Функция принимает значение movie_id, целое число и обновляет фильм с указанным id.
        Если такого фильма нет сообщает об этом.
        :param movie_id: int
        :return:
        """
        return MovieSchema().dump(movie_service.update_movie(movie_id, request.json))

    def delete(self, movie_id):
        """
        Функция принимает значение movie_id, целое число и удаляет фильм с указанным id..
        :param movie_id: int
        :return:
        """
        movie_service.delete(movie_id)
        return "", 204