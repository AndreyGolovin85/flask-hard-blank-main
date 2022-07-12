from flask_restx import Resource, Namespace

from dao.model.models_db import GenreSchema
from implemented import genre_service

genres_ns = Namespace("genres")


@genres_ns.route("/")
class GenresView(Resource):
    schema = GenreSchema(many=True)

    def get(self):
        return self.schema.dump(genre_service.get_genres()), 200


@genres_ns.route("/<int:gid>")
class GenreView(Resource):
    schema = GenreSchema()

    def get(self, gid):
        return self.schema.dump(genre_service.get_genres(gid)), 200
