import pathlib
import sys
from abc import ABC
from core.enum.database_type import DatabaseType
from core.enum.repository_type import RepositoryType
from src.core.tool.commons import log_init
from src.core.tool.properties import Properties


class AppConfigs(ABC):
    __root_dir = pathlib.Path(sys.argv[0]).parent.absolute()
    __log_file = "{}/../log/castlevania_inventory.log".format(__root_dir)
    __log = log_init(__log_file)
    __app_properties = Properties(load_dir="{}/resources".format(__root_dir))
    __log.info('Successfully read {} properties'.format(__app_properties.size()))
    __repository_type = RepositoryType[__app_properties.get('persistence.repository.type').upper()]
    __database_type = DatabaseType[__app_properties.get('persistence.database.type').upper()]
    __log.info('App configs loaded repository_type={} database_type={} root_dir={}'.format(
        __repository_type, __database_type, __root_dir))

    @staticmethod
    def get(property_name: str) -> str:
        return AppConfigs.__app_properties.get(property_name) if AppConfigs.__app_properties else None

    @staticmethod
    def get_int(property_name: str) -> int:
        return AppConfigs.__app_properties.get_int(property_name) if AppConfigs.__app_properties else None

    @staticmethod
    def get_float(property_name: str) -> float:
        return AppConfigs.__app_properties.get_float(property_name) if AppConfigs.__app_properties else None

    @staticmethod
    def get_bool(property_name: str) -> bool:
        return AppConfigs.__app_properties.get_bool(property_name) if AppConfigs.__app_properties else None

    @staticmethod
    def root_dir() -> str:
        return AppConfigs.__root_dir

    @staticmethod
    def log_file() -> str:
        return AppConfigs.__log_file

    @staticmethod
    def repository_type() -> RepositoryType:
        return AppConfigs.__repository_type

    @staticmethod
    def database_type() -> DatabaseType:
        return AppConfigs.__database_type
