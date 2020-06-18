import socket
from time import sleep

UDP_PORT = 12201
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.connect(('localhost', UDP_PORT))
while True:
	sock.send(b'{ "version": "1.1", "host": "example.org", "short_message": "A short message", "level": 5, "_some_info": "foo" }')
	sleep(1)
