from src.core.enum.database_type import DatabaseType
from src.core.enum.model_enum import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.service import Service
from src.model.item_model import Item


class ItemService(Service):
    def __init__(self, repository_type: RepositoryType, database_type: DatabaseType):
        super().__init__(repository_type, database_type, Model.ITEM)

    def save(self, item: Item):
        super().save(item)

    def remove(self, item: Item):
        super().remove(item)

    def get(self, entity_id: str) -> Item:
        entity = super().get(entity_id)
        item = Item()
        item.__dict__ = entity.__dict__
        return item
