import socket
from datetime import datetime

from python_education.logger.logger import create_logger

logger = create_logger()

"""
Низкоуровневая реализация (абстракция) сервера с использованием модуля socket. Сервер возвращает полученное от клиента сообщение.
Здесь нет никакого HTTP, только клиент-серверное взаимодействие по TCP. 
"""

def run_tcp_server():
    host = '127.0.0.1'
    port = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # чтобы не было ошибки [Errno 98] Address already in use
            server_socket.bind((host, port))
            server_socket.listen(5)

            logger.info(f"TCP server started on {host}:{port}")
            logger.info("Waiting for connections...")

            while True:
                try:
                    client_socket, client_address = server_socket.accept()
                    logger.info(f"New connection from {client_address}")

                    with client_socket:
                        while True:
                            data = client_socket.recv(1024)
                            if not data:
                                break

                            message = data.decode('utf-8')
                            logger.info(f"Received from {client_address}: {message}")

                            response = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Server received: {message}"
                            client_socket.send(response.encode('utf-8'))

                except ConnectionError as e:
                    logger.error(f"Connection error with {client_address}: {e}")
                except UnicodeDecodeError:
                    logger.error(f"Invalid data received from {client_address}")
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")

    except KeyboardInterrupt:
        logger.info("Server stopped by admin")
    except Exception as e:
        logger.error(f"Server error: {e}")


if __name__ == "__main__":
    run_tcp_server()