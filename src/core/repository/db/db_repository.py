from abc import abstractmethod
from core.config.app_configs import AppConfigs
from core.tool.commons import log_init
from src.core.factory.sql_factory import SqlFactory
from src.core.repository.repository import Repository


class DbRepository(Repository):
    def __init__(self, sql_factory: SqlFactory):
        super().__init__(sql_factory.sql_template_file)
        self.sql_factory = sql_factory
        self.hostname = AppConfigs.get('db.hostname')
        self.port = AppConfigs.get_int('db.port')
        self.user = AppConfigs.get('db.user')
        self.password = AppConfigs.get('db.password')
        self.database = AppConfigs.get('db.database')
        self.log = log_init(AppConfigs.log_file())
        self.connector = None
        self.cursor = None
        self.connect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def count(self):
        pass
