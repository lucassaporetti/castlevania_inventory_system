from src.core.factory.mysql.mysql_factory import MySqlFactory


class ItemFactory(MySqlFactory):

    sql_template_file = "sql/mysql/ddl/item_templates.properties"

    def __init__(self):
        super().__init__(ItemFactory.sql_template_file)
