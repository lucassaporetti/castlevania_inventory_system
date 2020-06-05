from src.core.factory.sql_factory import SqlFactory


class MySqlFactory(SqlFactory):
    def __init__(self, sql_template_file: str):
        super().__init__(sql_template_file)

    def count(self):
        return self.sql_templates.get('COUNT')

    def insert(self, values: dict):
        return self.sql_templates.get('INSERT').format(SqlFactory.dict_to_values(values))

    def update(self,  values: dict = None, filters: list = None):
        return self.sql_templates.get('UPDATE')\
            .format(
                SqlFactory.dict_to_field_set(values) if values is not None else '',
                SqlFactory.list_to_filters(filters, separator='') if filters is not None else '',
            )

    def delete(self, filters: list = None):
        return self.sql_templates.get('DELETE')\
            .format(
                SqlFactory.list_to_filters(filters, separator='') if filters is not None else '',
            )

    def select(self, columns: list = None, filters: list = None):
        return self.sql_templates.get('SELECT')\
            .format(
                SqlFactory.list_to_columns(columns) if columns is not None else '*',
                SqlFactory.list_to_filters(filters, separator='') if filters is not None else '',
            )
