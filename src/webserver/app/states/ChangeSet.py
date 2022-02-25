from typing import List


class Change:
    pass


class ChangeSet:

    __changes: List[Change]

    def __init__(self):
        self.__changes = list()

    def add(self, change: Change) -> None:
        self.__changes.append(change)
