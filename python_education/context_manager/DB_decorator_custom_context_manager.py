from contextlib import contextmanager

import psycopg2


@contextmanager
def connection_to_db(db_name: str):
    try:
        connection = psycopg2.connect(dbname="name", user="name", password="password", host='127.0.0.1')
        cursor = connection.cursor()
        yield cursor
    except psycopg2.OperationalError as e:
        print(f"Ошибка подключения к базе данных по причине: {e}")
    finally:
        cursor.close()
        connection.close()


class DataBase:
    def connection_to_db(self, db_name: str):
        with connection_to_db(db_name) as cursor:
            cursor.execute("SELECT * FROM goose_db_version where id = 1")
            for data in cursor.fetchall():
                print(data)


DataBase().connection_to_db("db_name")
