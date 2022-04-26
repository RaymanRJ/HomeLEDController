from tinydb import TinyDB, Query


class Database:

    __db: TinyDB

    def __init__(self, database_location: str = '/app/web-server-data/web-server-db.json'):
        self.__db = TinyDB(database_location)


db = Database()


def init_db():
    # If db contains documents, it is ready.
    pass
