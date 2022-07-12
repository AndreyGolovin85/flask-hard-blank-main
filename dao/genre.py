from dao.model.models_db import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_object(self, gid=None):
        query = self.session.query(Genre)
        if gid:
            return query.get(gid)
        return query.all()
