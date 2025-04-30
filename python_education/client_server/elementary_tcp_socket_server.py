import socket

host = "127.0.0.1"
port = 12345

server_sock = socket.socket()  # объект сервера
server_sock.bind((host, port))  # адрес сервера, по которому он будет прослушивать подключения
server_sock.listen(5)  # прослушивание подключений, максимум 5 в очереди (это первый сокет на сервере)

print("Socket server starts")
while True:
    client_sock, client_addr = server_sock.accept()  # accept() - метод для приема входящих подключений, client_sock - второй сокет на сервере
    data = client_sock.recv(1024)  # данные от клиента
    message_from_client = data.decode()  # преобразование данных в строку

    print("connection: ", client_sock)
    print("client address: ", client_addr)
    print(f"Client sent: {message_from_client}")

    message_to_client = f"Dear Client, your message '{message_from_client}'"  # сообщение для клиента
    client_sock.send(message_to_client.encode())  # отправка сообщения
    client_sock.close()  # закрытие подключения

print("Socket server stops")
server_sock.close()
