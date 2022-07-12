from dao.model.models_db import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_object(self, did=None):
        query = self.session.query(Director)
        if did:
            return query.get(did)
        return query.all()