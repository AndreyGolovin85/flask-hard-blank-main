from flask_restx import Resource, Namespace

from dao.model.models_db import DirectorSchema
from implemented import director_service

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    schema = DirectorSchema(many=True)

    def get(self):
        return self.schema.dump(director_service.get_director()), 200


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    schema = DirectorSchema()

    def get(self, did):
        return self.schema.dump(director_service.get_director(did)), 200
