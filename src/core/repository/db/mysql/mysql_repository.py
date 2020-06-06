import sys
import uuid
from abc import abstractmethod
from typing import Optional
import pymysql
from pymysql.err import OperationalError, ProgrammingError
from src.model.entity_model import Entity
from src.core.factory.sql_factory import SqlFactory
from src.core.repository.db.db_repository import DbRepository
from src.core.tool.commons import print_error


class MySqlRepository(DbRepository):
    __cache = {}

    def __init__(self, sql_factory: SqlFactory):
        super().__init__(sql_factory)

    def __str__(self):
        return "{}@{}:{}/{}".format(self.user, self.hostname, self.port, self.database)

    def is_connected(self):
        return self.connector is not None

    def connect(self):
        if not self.is_connected():
            cache_key = self.__str__()
            if cache_key in MySqlRepository.__cache:
                self.connector = MySqlRepository.__cache[cache_key]
                self.cursor = self.connector.cursor()
                assert self.is_connected(), "Not connected to the database"
            else:
                try:
                    self.connector = pymysql.connect(
                        host=self.hostname,
                        user=self.user,
                        port=self.port,
                        password=self.password,
                        database=self.database
                    )
                    assert self.is_connected(), "Not connected to the database"
                    self.cursor = self.connector.cursor()
                    self.log.info('Connected to {} established'.format(str(self)))
                    MySqlRepository.__cache[cache_key] = self.connector
                except OperationalError:
                    self.log.error('Unable to connect to {}'.format(str(self)))
                    print_error('Unable to connect to {}'.format(str(self)))
                    sys.exit(1)

    def disconnect(self):
        if self.is_connected():
            self.connector.close()
            self.connector = None
            self.log.info('Disconnected from {}.'.format(str(self)))
        else:
            self.log.error('Unable to disconnect from {}'.format(str(self)))
            sys.exit(1)

        return self.connector

    def count(self):
        count_stm = self.sql_factory.count()
        self.log.info('Executing SQL statement: {}'.format(count_stm))
        self.cursor.execute(count_stm)
        ret_val = self.cursor.fetchall()

        return ret_val

    def insert(self, entity: Entity):
        entity.entity_id = entity.entity_id if entity.entity_id is not None else str(uuid.uuid4())
        insert_stm = self.sql_factory.insert(entity.__dict__)
        self.log.info('Executing SQL statement: {}'.format(insert_stm))
        self.cursor.execute(insert_stm)
        self.connector.commit()

    def update(self, entity: Entity):
        update_stm = self.sql_factory.update(entity.__dict__, filters=[
            "UUID = '{}'".format(entity.entity_id)
        ])
        self.log.info('Executing SQL statement: {}'.format(update_stm))
        self.cursor.execute(update_stm)
        self.connector.commit()

    def delete(self, entity: Entity):
        delete_stm = self.sql_factory.delete(filters=[
            "UUID = '{}'".format(entity.entity_id)
        ])
        self.log.info('Executing SQL statement: {}'.format(delete_stm))
        self.cursor.execute(delete_stm)
        self.connector.commit()

    def find_all(self, filters: str = None) -> Optional[list]:
        if filters is not None:
            sql_filters = filters.upper().split(',')
        else:
            sql_filters = None
        select_stm = self.sql_factory.select(filters=sql_filters)
        self.log.info('Executing SQL statement: {}'.format(select_stm))
        try:
            self.cursor.execute(select_stm)
            result = self.cursor.fetchall()
            ret_val = []
            for next_row in result:
                ret_val.append(self.row_to_entity(next_row))
            return ret_val
        except ProgrammingError:
            return None

    def find_by_id(self, entity_id: str) -> Optional[Entity]:
        if entity_id:
            select_stm = self.sql_factory.select(filters=[
                "UUID = '{}'".format(entity_id)
            ])
            self.log.info('Executing SQL statement: {}'.format(select_stm))
            self.cursor.execute(select_stm)
            result = self.cursor.fetchall()
            return self.row_to_entity(result[0]) if len(result) > 0 else None
        else:
            return None

    @abstractmethod
    def row_to_entity(self, row: tuple) -> Entity:
        pass
