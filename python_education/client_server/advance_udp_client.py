import socket

from python_education.logger.logger import create_logger


logger = create_logger()

"""Клиент отправляет сообщение из консоли. В ответе сервер возвращает сообщение"""


def run_udp_client():
    host = '127.0.0.1'
    port = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as udp_socket:
            logger.info(f"UDP client ready to send to {host}:{port}")

            while True:
                message = input("Enter message (or 'exit' to quit): ")
                if message.lower() == 'exit':
                    break

                try:
                    # Отправляем сообщение серверу
                    udp_socket.sendto(message.encode('utf-8'), (host, port))

                    # Получаем ответ (таймаут 5 секунд)
                    udp_socket.settimeout(5.0)
                    response, server_address = udp_socket.recvfrom(1024)
                    logger.info(f"Server response: {response.decode('utf-8')}")

                except socket.timeout:
                    logger.error("No response from server (timeout)")
                except UnicodeError:
                    logger.error("Encoding/decoding error")
                except socket.error as e:
                    logger.error(f"Socket error: {e}")
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")

    except KeyboardInterrupt:
        logger.info("UDP client stopped by user")
    except Exception as e:
        logger.error(f"Client error: {e}")


if __name__ == "__main__":
    run_udp_client()