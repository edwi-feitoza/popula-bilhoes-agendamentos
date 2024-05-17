import mysql.connector as connector
import os

class AgendamentosDbConnection:
    def __init__(self):
        self.__db_host = os.getenv('DB_HOST')
        self.__db_database = os.getenv('DB_DATABASE')
        self.__db_user = os.getenv('DB_USER')
        self.__db_password = os.getenv('DB_PASSWORD')
        self.__connection = None

    def get_connection(self):
        try:
            db_connection = connector.connect(
                host=self.__db_host,
                database=self.__db_database,
                user=self.__db_user,
                password=self.__db_password
            )
            self.__connection = db_connection
            return db_connection
        except connector.Error as error:
            print('Failed to get database connect due to error {}'.format(error))

    def close_connection(self):
        if self.__connection.is_connected():
            self.__connection.close()
            print('MySQL Connection is closed now.')
