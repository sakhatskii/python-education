import logging

def create_logger() -> logging.Logger:
    file_log = logging.FileHandler('../tcp_socket.log')
    console_out = logging.StreamHandler()

    logging.basicConfig(
        handlers=(file_log, console_out),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
    )

    logger = logging.getLogger(__name__)
    return logger