import socket
from datetime import datetime

ENCODE = "UTF-8"
HOST = '127.0.0.1'
PORT = 5000
MAX_BYTES = 65535

def client():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dest = (HOST, PORT)
	text = input("Digite algum comando:\n")
	data = text.encode(ENCODE)
	sock.sendto(data, dest)
	print(sock.getsockname())
	data, address = sock.recvfrom(MAX_BYTES)
	text = data.decode(ENCODE)
	print(address, text)