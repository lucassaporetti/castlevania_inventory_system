from enum import Enum


class Attributes(Enum):
    NONE = 1
    HIT = 2
    CUT = 3
    CURSE = 4
    POISON = 5
    STONE = 6
    FIRE = 7
    ICE = 8
    THUNDER = 9
    HOLLY = 10
    DARK = 11

    def __str__(self):
        return self.name
