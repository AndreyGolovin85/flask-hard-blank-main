from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_movies(self, mid=None):
        return self.dao.get_object(mid)

    def get_movies_genre_or_director(self, **kwargs):
        return self.dao.get_object(**kwargs)

    def create_movie(self, data):
        return self.dao.create(data)

    def update_movie(self, movie_id, data):
        movie = self.get_movies(movie_id)

        movie.title = data["title"]
        movie.description = data["description"]
        movie.trailer = data["trailer"]
        movie.year = data["year"]
        movie.rating = data["rating"]
        movie.genre_id = data["genre_id"]
        movie.director_id = data["director_id"]

        self.dao.update(movie)
        return movie

    def update_movie_partial(self, movie_id, data):
        movie = self.get_movies(movie_id)

        if "title" in data:
            movie.title = data["title"]
        if "description" in data:
            movie.description = data["description"]
        if "trailer" in data:
            movie.trailer = data["trailer"]
        if "year" in data:
            movie.year = data["year"]
        if "rating" in data:
            movie.rating = data["rating"]
        if "genre_id" in data:
            movie.genre_id = data["genre_id"]
        if "director_id" in data:
            movie.director_id = data["director_id"]
        self.dao.update(movie)
        return movie

    def delete(self, movie_id):
        self.dao.delete(movie_id)

    def filter_movies_by_genre(self, genre_id):
        movies = self.get_movies_genre_or_director()
        result = []

        for movie in movies:
            if movie.genre_id == genre_id:
                result.append(movie)
        return result
