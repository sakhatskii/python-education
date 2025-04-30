import socket

host = "127.0.0.1"
port = 12345

client = socket.socket()
client.connect((host, port))  # подключение к серверу
data = client.recv(1024)  # получаем данные с сервера, размер буфера 1024
print("Server sent: ", data.decode())  # выводим данные на консоль
client.close()
