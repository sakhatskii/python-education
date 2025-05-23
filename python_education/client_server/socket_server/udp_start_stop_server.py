import socket
import threading
from typing import List

from python_education.logger.logger import create_logger

logger = create_logger()


class UDPServer(threading.Thread):
    """UDP сервер"""

    def __init__(self, host: str, port: int):
        super().__init__(daemon=True)
        self.host = host
        self.port = port
        self._stop_event = threading.Event()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._messages: List[str] = []

    def run(self) -> None:
        """Запуск UDP сервера и добавление сообщений в список"""
        try:
            self.socket.bind((self.host, self.port))
            logger.info(f"UDP server started on {self.host}:{self.port}")
            while not self._stop_event.is_set():
                try:
                    data, client_address = self.socket.recvfrom(1024)
                    message = data.decode("utf-8")
                    self._messages.append(message)
                    logger.info(f"Received from client {client_address}: {message}")
                except Exception as e:
                    logger.error(f"Unexpected error: {e}")
        except Exception as e:
            logger.error(f"UDP server error: {e}")

    def stop(self) -> None:
        """Остановка UDP сервера"""
        if not self._stop_event.is_set():
            self._stop_event.set()
            try:
                exit_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                exit_sock.sendto(b"", (self.host, self.port))
                exit_sock.close()
            except Exception as e:
                logger.error(f"Unexpected error: {e}")
            self.socket.close()
            logger.info("UDP server stopped")


if __name__ == "__main__":
    server = UDPServer("127.0.0.1", 12345)
    server.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop()
