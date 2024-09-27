import psycopg2

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = psycopg2.connect(dbname=self.db_name, user="user", password="password", host="127.0.0.1")
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
        self.cursor.close()

with DataBase("db_name") as cursor:
    cursor.execute("SELECT * FROM table_name where id = 1")
    for data in cursor.fetchall():
        print(data)
