from abc import ABC
from typing import Optional, Type
from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.enum.model_enum import Model
from src.core.enum.repository_type import RepositoryType
from src.core.repository.db.mysql.item_repository import ItemRepository as MysqlItemRepository
from src.core.repository.repository import Repository
from src.core.tool.commons import log_init

LOG = log_init(AppConfigs.log_file())


class RepositoryFacade(ABC):
    __cache = {}
    __repositories = {RepositoryType.DATABASE.name:
                      {DatabaseType.MYSQL.name:
                       {Model.ITEM.name: MysqlItemRepository}}}

    @staticmethod
    def create_or_get(repository_class: Type):
        cache_key = repository_class.__name__
        if cache_key in RepositoryFacade.__cache:
            LOG.info('Retrieving repository {}'.format(cache_key))
            return RepositoryFacade.__cache[cache_key]
        else:
            LOG.info('Creating repository {}'.format(cache_key))
            RepositoryFacade.__cache[cache_key] = repository_class()
            return RepositoryFacade.__cache[cache_key]

    @staticmethod
    def get(repository_type: RepositoryType, database_type: DatabaseType, model: Model) -> Optional[Repository]:
        repository_class = RepositoryFacade.__repositories[repository_type.name][database_type.name][model.name]
        repository = RepositoryFacade.create_or_get(repository_class)
        return repository
