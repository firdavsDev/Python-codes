import psycopg2
from psycopg2 import Error


class PostgresConnector:
    def __init__(self, db_name='postgres', password='2002', user='postgres', host='localhost', port='5432'):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name

    def __enter__(self):
        try:
            self.connection = psycopg2.connect(user = self.user, password = self.password, host = self.host,
                                               port = self.port, database = self.db_name)
            print("Connection open")
            return self
        except Error as err:
            print(f"Something wrong.\nFor more: {err}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
            print("Connection is closed")
