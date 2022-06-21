# variables
from db_credentials import datawarehouse_db_config, mysql_db_config
from sql_queries import mysql_queries

# methods
from etl import etl_process

def main():
    print('starting etl')

    # establish connection for target database (sql-server)
    target_cnx = pyodbc.connect(**datawarehouse_db_config)

    # mysql
    for config in mysql_db_config:
        try:
            print("loading db: " + config['database'])
            etl_process(mysql_queries, target_cnx, config, 'mysql')
        except Exception as error:
            print("etl for {} has error".format(config['database']))
            print('error message: {}'.format(error))
            continue

    target_cnx.close()

if __name__ == "__main__":
    main()