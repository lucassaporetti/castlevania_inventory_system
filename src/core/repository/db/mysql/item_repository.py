from src.core.enum.database_type import DatabaseType
from src.core.enum.model_enum import Model
from src.core.factory.sql_factory_facade import SqlFactoryFacade
from src.core.repository.db.mysql.mysql_repository import MySqlRepository
from src.model.item_model import Item
from src.model.entity_model import Entity


class ItemRepository(MySqlRepository):
    def __init__(self):
        super().__init__(SqlFactoryFacade.get(DatabaseType.MYSQL, Model.ITEM))

    def insert(self, item: Item):
        super().insert(item)

    def update(self, item: Item):
        super().update(item)

    def delete(self, item: Item):
        super().delete(item)

    def row_to_entity(self, row: tuple) -> Entity:
        return Item.of(list(row))
