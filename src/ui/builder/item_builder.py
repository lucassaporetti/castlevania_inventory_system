from src.core.enum.category_enum import Category
from src.core.enum.item_type_enum import ItemType
from src.core.enum.attributes_enum import Attributes
from src.core.enum.found_at_enum import FoundAt
from src.core.enum.dropped_by_enum import DroppedBy
from src.core.tool.commons import prompt, print_error
from src.core.tool.validators import validate_string, validate_enum, validate_int, validate_float
from src.model.item_model import Item


class ItemBuilder:
    def __init__(self):
        self.build()

    @staticmethod
    def build():
        valid = False
        item = name = category = item_type = description = \
            attributes = consume_mp = consume_heart = statistics_hp = \
            statistics_mp = statistics_heart = statistics_str = statistics_att = \
            statistics_gold = statistics_con = statistics_def = statistics_max_ht = \
            statistics_int = statistics_lck = statistics_max_hp = sell = found_at = \
            dropped_by = effect = image = animation = special_animation = None

        while not valid:
            name = prompt("Name: ", clear=True).strip() if name is None else name
            if not validate_string(name, "[a-zA-Z0-9]+", min_len=2):
                name = None
                print_error('Invalid name', name)
                continue
            category = prompt("Category: ").upper().replace('_', ' ').strip() if category is None else category
            if not validate_enum(category, Category):
                category = None
                print_error('Invalid category', category)
                continue
            item_type = prompt("Item type: ").upper().replace('_', ' ').strip() if item_type is None else item_type
            if not validate_enum(item_type, ItemType):
                item_type = None
                print_error('Invalid item type', item_type)
                continue
            description = prompt("Description: ") if description is None else description
            if not validate_string(description, "[a-zA-Z0-9]+", min_len=5, max_len=1000):
                description = None
                print_error('Invalid description', description)
                continue
            attributes = prompt("Attributes: ").upper().replace('_', ' ').strip() if attributes is None else attributes
            if not validate_enum(attributes, Attributes):
                attributes = None
                print_error('Invalid attributes', attributes)
                continue
            consume_mp = prompt("Consume MP: ").strip() if consume_mp is None else consume_mp
            if not validate_int(consume_mp, max_value=1000):
                consume_mp = None
                print_error('Invalid consume MP', consume_mp)
                continue
            consume_heart = prompt("Consume Heart: ").strip() if consume_heart is None else consume_heart
            if not validate_int(consume_heart, max_value=1000):
                consume_heart = None
                print_error('Invalid consume heart', consume_heart)
                continue
            statistics_hp = prompt("statistics_hp: ").strip() if statistics_hp is None else statistics_hp
            if not validate_int(statistics_hp, max_value=1000):
                statistics_hp = None
                print_error('Invalid statistics_hp', statistics_hp)
                continue
            statistics_mp = prompt("statistics_mp: ").strip() if statistics_mp is None else statistics_mp
            if not validate_int(statistics_mp, max_value=1000):
                statistics_mp = None
                print_error('Invalid statistics_mp', statistics_mp)
                continue
            statistics_heart = prompt("statistics_heart: ").strip() if statistics_heart is None else statistics_heart
            if not validate_int(statistics_heart, max_value=1000):
                statistics_heart = None
                print_error('Invalid statistics_heart', statistics_heart)
                continue
            statistics_str = prompt("statistics_str: ").strip() if statistics_str is None else statistics_str
            if not validate_int(statistics_str, max_value=1000):
                statistics_str = None
                print_error('Invalid statistics_str', statistics_str)
                continue
            statistics_att = prompt("statistics_att: ").strip() if statistics_att is None else statistics_att
            if not validate_int(statistics_att, max_value=1000):
                statistics_att = None
                print_error('Invalid statistics_att', statistics_att)
                continue
            statistics_gold = prompt("statistics_gold: ").strip() if statistics_gold is None else statistics_gold
            if not validate_int(statistics_gold, max_value=1000):
                statistics_gold = None
                print_error('Invalid statistics_gold', statistics_gold)
                continue
            statistics_con = prompt("statistics_con: ").strip() if statistics_con is None else statistics_con
            if not validate_int(statistics_con, max_value=1000):
                statistics_con = None
                print_error('Invalid statistics_con', statistics_con)
                continue
            statistics_def = prompt("statistics_def: ").strip() if statistics_def is None else statistics_def
            if not validate_int(statistics_def, max_value=1000):
                statistics_def = None
                print_error('Invalid statistics_def', statistics_def)
                continue
            statistics_max_ht = prompt("statistics_max_ht: ").strip() if statistics_max_ht is None else statistics_max_ht
            if not validate_int(statistics_max_ht, max_value=1000):
                statistics_max_ht = None
                print_error('Invalid statistics_max_ht', statistics_max_ht)
                continue
            statistics_int = prompt("statistics_int: ").strip() if statistics_int is None else statistics_int
            if not validate_int(statistics_int, max_value=1000):
                statistics_int = None
                print_error('Invalid statistics_int', statistics_int)
                continue
            statistics_lck = prompt("statistics_lck: ").strip() if statistics_lck is None else statistics_lck
            if not validate_int(statistics_lck, max_value=1000):
                statistics_lck = None
                print_error('Invalid statistics_lck', statistics_lck)
                continue
            statistics_max_hp = prompt("statistics_max_hp: ").strip() if statistics_max_hp is None else statistics_max_hp
            if not validate_int(statistics_max_hp, max_value=1000):
                statistics_max_hp = None
                print_error('Invalid statistics_max_hp', statistics_max_hp)
                continue
            sell = prompt("Sell: $").strip() if sell is None else sell
            if not validate_float(sell, max_value=1000000.0):
                sell = None
                print_error('Invalid sell', sell)
                continue
            found_at = prompt("Found_at: ").upper().replace('_', ' ').strip() if found_at is None else found_at
            if not validate_enum(found_at, FoundAt):
                found_at = None
                print_error('Invalid found at', found_at)
                continue
            dropped_by = prompt("Dropped by: ").upper().replace('_', ' ').strip() if dropped_by is None else dropped_by
            if not validate_enum(dropped_by, DroppedBy):
                dropped_by = None
                print_error('Invalid dropped by', dropped_by)
                continue
            effect = prompt("Effect: ") if effect is None else effect
            if not validate_string(effect, "[a-zA-Z0-9]+", min_len=5, max_len=1000):
                effect = None
                print_error('Invalid effect', effect)
                continue
            image = prompt("Image: ") if image is None else image
            if not validate_string(image, "[a-zA-Z0-9]+", min_len=5, max_len=1000):
                image = None
                print_error('Invalid image', image)
                continue
            animation = prompt("Animation: ") if animation is None else animation
            if not validate_string(animation, "[a-zA-Z0-9]+", min_len=5, max_len=1000):
                animation = None
                print_error('Invalid animation', animation)
                continue
            special_animation = prompt("Special animation: ") if special_animation is None else special_animation
            if not validate_string(special_animation, "[a-zA-Z0-9]+", min_len=5, max_len=1000):
                special_animation = None
                print_error('Invalid special animation', special_animation)
                continue
            valid = True
            item = Item.Builder()\
                .with_name(name)\
                .with_category(category)\
                .with_item_type(item_type)\
                .with_description(description)\
                .with_attributes(attributes)\
                .with_consume_mp(consume_mp)\
                .with_consume_heart(consume_heart)\
                .with_statistics_hp(statistics_hp)\
                .with_statistics_mp(statistics_mp)\
                .with_statistics_heart(statistics_heart)\
                .with_statistics_str(statistics_str)\
                .with_statistics_att(statistics_att)\
                .with_statistics_gold(statistics_gold)\
                .with_statistics_con(statistics_con)\
                .with_statistics_def(statistics_def)\
                .with_statistics_max_ht(statistics_max_ht)\
                .with_statistics_int(statistics_int)\
                .with_statistics_lck(statistics_lck)\
                .with_statistics_max_hp(statistics_max_hp)\
                .with_sell(sell)\
                .with_found_at(found_at)\
                .with_dropped_by(dropped_by)\
                .with_effect(effect)\
                .with_image(image)\
                .with_animation(animation)\
                .with_special_animation(special_animation)\
                .build()

        return item
