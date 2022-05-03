from abc import ABC, abstractmethod


class Table(ABC):

    @classmethod
    @abstractmethod
    def create_table_string(cls):
        pass
