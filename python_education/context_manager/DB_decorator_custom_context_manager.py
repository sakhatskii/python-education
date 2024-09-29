from contextlib import contextmanager

import psycopg2


@contextmanager  # декоратор для создания контекстного менеджера
def connection_to_db(db_name: str):
    try:
        connection = psycopg2.connect(dbname="name", user="name", password="password", host='127.0.0.1')  # подключаемся к бд
        cursor = connection.cursor()  # создаем курсор для выполнения запросов
        yield cursor  # возвращаем курсор для использования в блоке with
    except psycopg2.OperationalError as e:
        print(f"Ошибка подключения к базе данных по причине: {e}")  # выводим сообщение в случае сбоя подключения к бд
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
