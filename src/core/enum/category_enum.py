from enum import Enum


class Category(Enum):
    WEAPON = 1
    SHIELD = 2
    ARMOR_CLOTHE = 3
    RELIC = 4
    SPELL = 5
    OTHER = 6
    CONSUMABLE = 7
    STANDARD = 8

    def __str__(self):
        return self.name
