import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 12201

print("UDP target IP: ", UDP_IP)
print("UDP target port: ", UDP_PORT)

for i in range(50000):
	MESSAGE = '{ "version": "1.1", "host": "example.org", "short_message": "A short'+str(i).encode("utf-8").decode("utf-8")+' message", "level": 5, "_some_info": "foo" }'
	print("message:", MESSAGE)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # UDP
	sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))
