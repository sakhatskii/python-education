import threading
from http.server import HTTPServer

import pytest

from python_education.client_server.http_server.http_server import SimpleHTTPRequestHandler


@pytest.fixture(scope="session")
def http_server():
    server = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    yield
    server.shutdown()
    thread.join()
