from typing import Dict, Callable

from tinydb import TinyDB, Query


class Database:

    __db: TinyDB

    def __init__(self, database_location: str = '/app/web-server-data/web-server-db.json'):
        self.__db = TinyDB(database_location)

    def insert(self, document: Dict):
        self.__db.insert(document)

    def search(self, func: bool):
        print(func)
        func
        return self.__db.search(func)


db = Database()


def init_db():
    db.insert({'name': 'John', 'age': 22})
    User = Query()
    print(db.search(User.name == 'John'))

init_db()
