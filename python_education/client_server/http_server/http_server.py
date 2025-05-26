import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from python_education.logger.logger import create_logger

logger = create_logger()

"""
Реализация простого HTTP-сервера с использованием модуля http.server. 

HTTPServer - базовый класс для HTTP-сервера.
BaseHTTPRequestHandler - базовый класс для обработки HTTP-запросов.

send_response(200) - отправляет код статуса 200 (OK),
send_header() - добавляет HTTP-заголовок,
end_headers() - завершает заголовки,
wfile.write() - отправляет тело ответа (должно быть в байтах).

rfile.read(size) - доступ к телу запроса. Функции должен быть явно передан размер, иначе запрос будет висеть и никогда не закончится.
Size (content_length) может быть извлечен через headers и преобразован в целое число.

serve_forever() запускает бесконечный цикл обработки запросов.
"""


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):  # curl -X GET http://127.0.0.1:8000
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, world!")

    def do_POST(self):  # curl -X POST -d '{"name": "ALEX"}' http://127.0.0.1:8000
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        response = {"message": f"Hello, {data['name']}!"}

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logger.info(f"Starting httpd server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
