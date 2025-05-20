import socket
from datetime import datetime

from python_education.logger.logger import create_logger

logger = create_logger()

"""
Низкоуровневая реализация (абстракция) сервера с использованием модуля socket. Сервер возвращает полученное от клиента сообщение.
Здесь нет никакого HTTP, только клиент-серверное взаимодействие по UDP.
"""


def run_udp_server():
    host = '127.0.0.1'
    port = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:  # socket.SOCK_DGRAM для UDP
            udp_socket.bind((host, port))  # метод listen тут уже не нужен

            logger.info(f"UDP server started on {host}:{port}")
            logger.info("Waiting for connections...")

            while True:
                try:
                    data, client_address = udp_socket.recvfrom(1024)
                    if not data:
                        continue

                    message = data.decode('utf-8')
                    logger.info(f"Received from {client_address}: {message}")

                    response = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] UDP Server received: {message}"

                    udp_socket.sendto(response.encode('utf-8'), client_address)

                except UnicodeDecodeError:
                    logger.error(f"Invalid data received from {client_address}")
                except socket.error as e:
                    logger.error(f"Socket error: {e}")
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")

    except KeyboardInterrupt:
        logger.info("UDP server stopped by admin")
    except Exception as e:
        logger.error(f"Server startup error: {e}")


if __name__ == "__main__":
    run_udp_server()
