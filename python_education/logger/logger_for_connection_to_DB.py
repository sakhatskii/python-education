import psycopg2
import logging

file_log = logging.FileHandler('../DB_connection.log')  # запись логов в файл
console_out = logging.StreamHandler()  # вывод логов в консоль

# настройка логгера
logging.basicConfig(
    handlers=(file_log, console_out),
    level=logging.INFO,  # минимальный уровень логирования
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'  # формат вывода логов
)

logger = logging.getLogger(__name__)  # создаем логгер с именем текущего модуля (logger_for_connection_to_DB.py)

class DataBase:
    def connection_to_db(self, name: str, password: str):
        logger.info("Функция connection_to_db вызвана с аргументами: %s, %s", name, password)
        try:
            # подключаемся к бд
            connection = psycopg2.connect(dbname=name, user="user", password=password, host="127.0.0.1")
            with connection:
                # создаем курсор для выполнения запросов
                cursor = connection.cursor()
                # выполняем sql запрос
                cursor.execute("SELECT * FROM name_table where id = 1")
                # получаем результаты запроса
                result = cursor.fetchall()
                # выводим результаты
                for data in result:
                    print(data)
                # cursor.close() и connection.close() не нужны, т.к with сам закрывает соединения
        except Exception as e:
            # выводим сообщение в случае сбоя подключения к бд
            logger.error(f"Ошибка подключения к базе данных {e}")

DataBase().connection_to_db("db_name","password")
