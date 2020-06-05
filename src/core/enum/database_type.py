from enum import Enum


class DatabaseType(Enum):
    ARCHIVE = 1
    MYSQL = 2

    def __str__(self):
        return "{}".format(self.name.upper())
