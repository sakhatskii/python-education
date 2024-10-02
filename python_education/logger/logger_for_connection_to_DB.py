import psycopg2
import logging

file_log = logging.FileHandler('../DB_connection.log')
console_out = logging.StreamHandler()

logging.basicConfig(
    handlers=(file_log, console_out),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

logger = logging.getLogger(__name__)


class DataBase:
    def connection_to_db(self, name: str, password: str):
        logger.info("Функция connection_to_db вызвана с аргументами: %s, %s", name, password)
        try:
            connection = psycopg2.connect(dbname=name, user="user", password=password, host="127.0.0.1")
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM name_table where id = 1")
                result = cursor.fetchall()
                for data in result:
                    print(data)
        except Exception as e:
            logger.error(f"Ошибка подключения к базе данных по причине: {e}")


DataBase().connection_to_db("db_name", "password")
