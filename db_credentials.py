datawarehouse_name = 'etl-python'

# sql-server (target db, datawarehouse)
datawarehouse_db_config = {
    'Trusted_Connection': 'yes',
    'driver': '{SQL Server}',
    'server': 'datawarehouse_sql_server',
    'database': '{}'.format(datawarehouse_name),
    'user': 'user_test',
    'password': 'test1234',
    'autocommit': True,
}

# sql-server (source db)
sqlserver_db_config = [
    {
        'Trusted_Connection': 'yes',
        'driver': '{SQL Server}',
        'server': 'datawarehouse_sql_server',
        'database': 'db1',
        'user': 'user_test',
        'password': 'test1234',
        'autocommit': True,
    }
]

# mysql (source db)
mysql_db_config = [
    {
        'user': 'user_test',
        'password': 'test1234',
        'host': 'localhost',
        'database': 'sakila',
    },
]

# firebird (source db)
fdb_db_config = [
    {
        'dsn': "./meta/sakila-schema.sql",
        'user': "user_test",
        'password': "test1234"
    }
]