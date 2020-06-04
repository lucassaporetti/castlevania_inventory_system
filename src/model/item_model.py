import uuid
from src.model.entity_model import Entity
from src.core.enum.category_enum import Category
from src.core.enum.type_enum import Type
from src.core.enum.attributes_enum import Attributes
from src.core.enum.found_at_enum import FoundAt
from src.core.enum.dropped_by_enum import DroppedBy


class Item(Entity):
    # @staticmethod
    # def of(values: list):
    #     return Item(
    #         str(values[0]), str(values[1]), str(values[2]),
    #         Color[values[3]], int(values[4]), Fuel[values[5]],
    #         str(values[6]), float(values[7]), YesNo(values[8])
    #     )
    def __init__(self, entity_id: str = None, name: str = None, category: Category = None, type: Type = None,
                 description: str = None, attributes: Attributes = None, consume_mp: int = None,
                 consume_heart: int = None, statistics_hp: int = None, statistics_mp: int = None,
                 statistics_heart: int = None, statistics_str: int = None, statistics_att: int = None,
                 statistics_gold: int = None, statistics_con: int = None, statistics_def: int = None,
                 statistics_max_ht: int = None, statistics_int: int = None, statistics_lck: int = None,
                 statistics_max_hp: int = None, sell: float = None, found_at: FoundAt = None,
                 dropped_by: DroppedBy = None, effect: str = None, image: str = None, animation: str = None,
                 special_animation: str = None):
        super().__init__(entity_id)
        self.name = name
        self.category = category
        self.type = type
        self.description = description
        self.attributes = attributes
        self.consume_mp = consume_mp
        self.consume_heart = consume_heart
        self.statistics_hp = statistics_hp
        self.statistics_mp = statistics_mp
        self.statistics_heart = statistics_heart
        self.statistics_str = statistics_str
        self.statistics_att = statistics_att
        self.statistics_gold = statistics_gold
        self.statistics_con = statistics_con
        self.statistics_def = statistics_def
        self.statistics_max_ht = statistics_max_ht
        self.statistics_int = statistics_int
        self.statistics_lck = statistics_lck
        self.statistics_max_hp = statistics_max_hp
        self.sell = sell
        self.found_at = found_at
        self.dropped_by = dropped_by
        self.effect = effect
        self.image = image
        self.animation = animation
        self.special_animation = special_animation

    def __str__(self):
        return "{} | {} | {} | {} | {} | {} | {} | {} | {} | {}" \
               "{} | {} | {} | {} | {} | {} | {} | {} | {} | {}" \
               "{} | {} | {} | {} | {}".format(
                super().__str__(), self.name, self.category.name, self.type.name, self.description,
                self.attributes.name, self.consume_mp, self.consume_heart, self.statistics_hp, self.statistics_mp,
                self.statistics_heart, self.statistics_str, self.statistics_att, self.statistics_gold,
                self.statistics_con, self.statistics_def, self.statistics_max_ht, self.statistics_int,
                self.statistics_lck, self.statistics_max_hp, self.sell, self.found_at.name, self.dropped_by.name,
                self.effect, self.image, self.animation, self.special_animation)

    class Builder:
        def __init__(self):
            self.entity_id = str(uuid.uuid4())
            self.name = None
            self.category = None
            self.type = None
            self.description = None
            self.attributes = None
            self.consume_mp = None
            self.consume_heart = None
            self.statistics_hp = None
            self.statistics_mp = None
            self.statistics_heart = None
            self.statistics_str = None
            self.statistics_att = None
            self.statistics_gold = None
            self.statistics_con = None
            self.statistics_def = None
            self.statistics_max_ht = None
            self.statistics_int = None
            self.statistics_lck = None
            self.statistics_max_hp = None
            self.sell = None
            self.found_at = None
            self.dropped_by = None
            self.effect = None
            self.image = None
            self.animation = None
            self.special_animation = None

        def with_name(self, name: str):
            self.name = name
            return self

        def with_category(self, category: Category):
            self.category = category
            return self

        def with_type(self, type: Type):
            self.type = type
            return self

        def with_description(self, description: str):
            self.description = description
            return self

        def with_attributes(self, attributes: Attributes):
            self.attributes = attributes
            return self

        def with_consume_mp(self, consume_mp: int):
            self.consume_mp = consume_mp
            return self

        def with_consume_heart(self, consume_heart: int):
            self.consume_heart = consume_heart
            return self

        def with_statistics_hp(self, statistics_hp: int):
            self.statistics_hp = statistics_hp
            return self

        def with_statistics_mp(self, statistics_mp: int):
            self.statistics_mp = statistics_mp
            return self

        def with_statistics_heart(self, statistics_heart: int):
            self.statistics_heart = statistics_heart
            return self

        def with_statistics_str(self, statistics_str: int):
            self.statistics_str = statistics_str
            return self

        def with_statistics_att(self, statistics_att: int):
            self.statistics_att = statistics_att
            return self

        def with_statistics_gold(self, statistics_gold: int):
            self.statistics_gold = statistics_gold
            return self

        def with_statistics_con(self, statistics_con: int):
            self.statistics_con = statistics_con
            return self

        def with_statistics_def(self, statistics_def: int):
            self.statistics_def = statistics_def
            return self

        def with_statistics_max_ht(self, statistics_max_ht: int):
            self.statistics_max_ht = statistics_max_ht
            return self

        def with_statistics_int(self, statistics_int: int):
            self.statistics_int = statistics_int
            return self

        def with_statistics_lck(self, statistics_lck: int):
            self.statistics_lck = statistics_lck
            return self

        def with_statistics_max_hp(self, statistics_max_hp: int):
            self.statistics_max_hp = statistics_max_hp
            return self

        def with_sell(self, sell: float):
            self.sell = sell
            return self

        def with_found_at(self, found_at: FoundAt):
            self.found_at = found_at
            return self

        def with_dropped_by(self, dropped_by: DroppedBy):
            self.dropped_by = dropped_by
            return self

        def with_effect(self, effect: str):
            self.effect = effect
            return self

        def with_image(self, image: str):
            self.image = image
            return self

        def with_animation(self, animation: str):
            self.animation = animation
            return self

        def with_special_animation(self, special_animation: str):
            self.special_animation = special_animation
            return self

        def build(self):
            return Item(self.entity_id, self.name, self.category, self.type, self.description, self.attributes,
                        self.consume_mp, self.consume_heart, self.statistics_hp, self.statistics_mp,
                        self.statistics_heart, self.statistics_str, self.statistics_att, self.statistics_gold,
                        self.statistics_con, self.statistics_def, self.statistics_max_ht, self.statistics_int,
                        self.statistics_lck, self.statistics_max_hp, self.sell, self.found_at, self.dropped_by,
                        self.effect, self.image, self.animation, self.special_animation)
