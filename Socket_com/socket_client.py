import socket
from info import ip_addr, port

HOST = ip_addr
PORT = port

# num = bytes(b"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
num = "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"
# num = bytes(num, encoding='utf-8')
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

client_socket.sendall(num.encode())
# client_socket.sendall(num)
# client_socket.sendall(num.encode('utf-8'))

data = client_socket.recv(180)
# received = str(data, encoding="utf-8")
print("Received", repr(data.decode()))
# print("Received", repr(received))

client_socket.close()
