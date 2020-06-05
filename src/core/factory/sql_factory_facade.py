from abc import ABC
from typing import Optional, Type
from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.factory.mysql.item_factory import ItemFactory as MysqlItemFactory
from src.core.factory.sql_factory import SqlFactory
from src.core.tool.commons import log_init
from src.core.enum.model_enum import Model

LOG = log_init(AppConfigs.log_file())


class SqlFactoryFacade(ABC):
    __cache = {}
    __factories = {
        DatabaseType.MYSQL.name: {Model.ITEM.name: MysqlItemFactory}}

    @staticmethod
    def create_or_get(factory_class: Type):
        cache_key = factory_class.__name__
        if cache_key in SqlFactoryFacade.__cache:
            LOG.info('Retrieving factory {}'.format(cache_key))
            return SqlFactoryFacade.__cache[cache_key]
        else:
            LOG.info('Creating factory {}'.format(cache_key))
            SqlFactoryFacade.__cache[cache_key] = factory_class()
            return SqlFactoryFacade.__cache[cache_key]

    @staticmethod
    def get(database_type: DatabaseType, model: Model) -> Optional[SqlFactory]:
        factory_class = SqlFactoryFacade.__factories[database_type.name][model.name]
        factory = SqlFactoryFacade.create_or_get(factory_class)
        return factory
