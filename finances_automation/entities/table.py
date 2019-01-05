import pandas as pd

from finances_automation import configuration as conf


class Table:

    def __init__(self, name, schema, type, monetary_columns=None, date_columns=None,
                 date_format=None, category_columns=None):
        """ Initialise a python representation of a database table in memory.

        :param str name: name of table
        :param str type: type of table
        :param dict schema: schema of table as a dictionary mapping column name to PostgreSQL type
            as a string
        :param list(str) monetary_columns: names of columns containing monetary amounts
        :param list(str) date_columns: names of columns containing dates
        :param str date_format: format of dates in table
        :param list(str) category_columns: names of columns containing category information

        :var pd.DataFrame data: data loaded from the database table (modified or unmodified)
        """
        self.name = name
        self.type = type
        self.schema = schema
        self.monetary_columns = monetary_columns
        self.date_columns = date_columns
        self.date_format = date_format
        self.category_columns = category_columns

        self.data = pd.DataFrame()

    @staticmethod
    def check_types(name, type, schema, monetary_columns, date_columns, date_format,
                    category_columns):
        """ Check if the initialisation parameters for the Table are of the correct type.

        :raise TypeError: if any of the parameters are of the wrong type
        """
        if not isinstance(name, str):
            raise TypeError('name should be a string.')
        if not isinstance(type, str):
            raise TypeError('type should be a string')
        if not isinstance(schema, dict):
            raise TypeError('schema should be a dictionary.')
        if not isinstance(monetary_columns, list):
            raise TypeError('monetary_columns should be a list of strings.')
        if not isinstance(date_columns, list):
            raise TypeError('date_columns should be a list of strings.')
        if not isinstance(date_format, str):
            raise TypeError('date_format should be a string.')
        if not isinstance(category_columns, list):
            raise TypeError('category_columns should be a list of strings.')

    @staticmethod
    def get_table(table_name):
        """ Get a Table object for table_name if its configuration exists in the configuration file.

        :param str table_name: possible name of a table

        :raise ValueError: if the a configuration doesn't exist for the table name
        :return Table:
        """
        try:
            table_conf = conf.table_configurations[table_name]
            return Table(**table_conf)

        except KeyError:
            raise ValueError(
                "No such table: '{}'. Possible tables: {}"
                .format(table_name, conf.table_names)
            )
