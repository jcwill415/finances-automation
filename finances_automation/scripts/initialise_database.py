from finances_automation.database import Database
from finances_automation.scripts import configuration as conf


OVERWRITE = True

CREATE_TRANSACTIONS_TABLE = (
    """
        CREATE TABLE {} (
             {} serial PRIMARY KEY,
             {} DATE NOT NULL,
             {} VARCHAR,
             {} VARCHAR,
             {} DECIMAL,
             {} DECIMAL,
             {} DECIMAL NOT NULL,
             {} INT,
             {} VARCHAR
        );
    """
    .format(conf.DB_NAME, *conf.TABLE_HEADERS)
)


def initialise_finances_database(db_name, db_cluster, user, table_creation_query):
    """ Create and initialise finances database with empty transactions table.
    """
    database = Database(db_name, db_cluster, user)
    database.create(overwrite=True)
    database.start()
    database.execute_statement(table_creation_query)
    database.stop()


if __name__ == '__main__':
    initialise_finances_database(
        conf.DB_NAME,
        conf.DB_CLUSTER,
        conf.USER,
        CREATE_TRANSACTIONS_TABLE
    )
