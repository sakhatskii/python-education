import psycopg2
import logging

file_log = logging.FileHandler('../DB_connection.log')  # запись логов в файл DB_connection.log
console_out = logging.StreamHandler()  # вывод логов в консоль

logging.basicConfig(  # настройка логгера
    handlers=(file_log, console_out),
    level=logging.INFO,  # минимальный уровень логирования
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'  # формат вывода логов
)

logger = logging.getLogger(__name__)  # создаем логгер с именем текущего модуля (logger_for_connection_to_DB.py)


class DataBase:
    def connection_to_db(self, name: str, password: str):
        logger.info("Функция connection_to_db вызвана с аргументами: %s, %s", name, password)
        try:
            connection = psycopg2.connect(dbname=name, user="user", password=password, host="127.0.0.1")  # подключаемся к бд
            with connection:
                cursor = connection.cursor()  # создаем курсор для выполнения запросов
                cursor.execute("SELECT * FROM name_table where id = 1")  # выполняем sql запрос
                result = cursor.fetchall()  # получаем результаты запроса
                for data in result:  # выводим результаты
                    print(data)
        except Exception as e:
            logger.error(f"Ошибка подключения к базе данных по причине: {e}")  # выводим сообщение в случае сбоя подключения к бд


DataBase().connection_to_db("db_name", "password")
