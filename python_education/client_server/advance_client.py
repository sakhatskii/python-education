import socket
import logging

from python_education.logger.logger import create_logger


logger = create_logger()

"""Клиент отправляет сообщение из консоли. В ответе сервер возвращает сообщение"""

def run_tcp_client():
    host = '127.0.0.1'
    port = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            try:
                client_socket.connect((host, port))
                logger.info(f"Connected to server {host}:{port}")

                while True:
                    message = input("Enter message (or 'exit' to quit): ")
                    if message.lower() == 'exit':
                        break

                    try:
                        client_socket.send(message.encode('utf-8'))
                        response = client_socket.recv(1024)
                        logger.info(f"Server response: {response.decode('utf-8')}")
                    except ConnectionError:
                        logger.error("Connection lost with server")
                        break

            except ConnectionRefusedError:
                logger.error("Could not connect to server. Is it running?")
            except Exception as e:
                logger.error(f"Connection error: {e}")

    except KeyboardInterrupt:
        logger.info("Client stopped by user")
    except Exception as e:
        logger.error(f"Client error: {e}")


if __name__ == "__main__":
    run_tcp_client()