import sqlite3
from sqlite3 import Cursor

from app.models.LEDs.LEDCabinetLocation import LEDCabinetLocation


class Database:

    __db: sqlite3
    __cur: Cursor

    def __init__(self, database_location: str = '/app/web-server-data/web-server-db.json'):
        self.__db = sqlite3.connect(database_location)
        self.__cur = self.__db.cursor()

    def execute(self, command: str):
        return self.__cur.execute(command)

    def commit(self):
        return self.__db().commit()


db = Database()


def init_db():
    db.execute(LEDCabinetLocation.create_table_string())
    db.commit()
    pass

init_db()