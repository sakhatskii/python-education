import socket

"""Здесь сервер принимает клиента, выводит информацию о его подключении и отправляет клиенту в ответ строку 'Hello Client!'"""

host = "127.0.0.1"
port = 12345

server_sock = socket.socket()  # объект сервера
server_sock.bind((host, port))  # адрес сервера, по которому он будет прослушивать подключения
server_sock.listen(5)  # прослушивание подключений, максимум 5 в очереди (это первый сокет на сервере)

print("Socket server starts")

client_sock, client_addr = server_sock.accept()  # accept() - метод для приема входящих подключений, client_sock - второй сокет на сервере

print("connection: ", client_sock)
print("client address: ", client_addr)

message = "Hello Client!"  # сообщение для клиента
client_sock.send(message.encode())  # отправка сообщения
client_sock.close()  # закрытие подключения

print("Socket server stops")
server_sock.close()
