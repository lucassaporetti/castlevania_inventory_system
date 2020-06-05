from abc import ABC
from typing import Type
from core.config.app_configs import AppConfigs
from src.core.enum.database_type import DatabaseType
from src.core.enum.model_enum import Model
from src.core.enum.repository_type import RepositoryType
from src.core.service.item_service import ItemService
from src.core.service.service import Service
from src.core.tool.commons import log_init

LOG = log_init(AppConfigs.log_file())


class ServiceFacade(ABC):
    __cache = {}
    __services = {Model.ITEM.name: ItemService}

    @staticmethod
    def create_or_get(service_class: Type, repository_type: RepositoryType, database_type: DatabaseType):
        cache_key = service_class.__name__
        if cache_key in ServiceFacade.__cache:
            LOG.info('Retrieving service {}'.format(cache_key))
            return ServiceFacade.__cache[cache_key]
        else:
            LOG.info('Creating service {}'.format(cache_key))
            ServiceFacade.__cache[cache_key] = service_class(repository_type, database_type)
            return ServiceFacade.__cache[cache_key]

    @staticmethod
    def get(repository_type: RepositoryType, database_type: DatabaseType, model: Model) -> Service:
        service_class = ServiceFacade.__services[model.name]
        service = ServiceFacade.create_or_get(service_class, repository_type, database_type)
        LOG.info('Retrieving service: {}'.format(service))
        return service

    @staticmethod
    def get_item_service() -> Service:
        return ServiceFacade.get(AppConfigs.repository_type(), AppConfigs.database_type(), Model.ITEM)
