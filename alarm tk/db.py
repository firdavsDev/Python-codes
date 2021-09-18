import psycopg2
from psycopg2 import Error


class PostConnect:
    def __init__(self, db_name: str = 'Bozor',
                 user: str = 'postgres',
                 pswd: str = '2002',
                 host: str = 'localhost',
                 port: str = '5432'):
        self.db_name = db_name
        self.user = user
        self.pswd = pswd
        self.host = host
        self.port = port

    def __enter__(self):
        try:
            self.conn = psycopg2.connect(user=self.user,
                                         password=self.pswd,
                                         host=self.host,
                                         port=self.port,
                                         database=self.db_name)
            print("Connection opened :)")
            self.cur = self.conn.cursor()

            return self
        except (Error, Exception) as e:
            print("Error occur", e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Connected close : ")
        if self.conn:
            self.cur.close()
            self.conn.close()
            

