from dao.model.models_db import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_object(self):
        query = self.session.query(Movie)
        return query.all()

    def filter_object(self, **kwargs):
        query = self.session.query(Movie)
        for key, value in kwargs.items():
            query = query.filter(eval(f"Movie.{key}") == int(value))
            print(type(query.all()))
            return query.all()

    def one_movie(self, mid):
        query = self.session.query(Movie)
        return query.get(mid)

    def create(self, data):
        new_movie = Movie(**data)
        with self.session.begin():
            self.session.add(new_movie)
        return new_movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid):
        movie = self.one_movie(mid)
        if not movie:
            return "", 404
        self.session.delete(movie)
        self.session.commit()
