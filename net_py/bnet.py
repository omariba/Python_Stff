import socket

target = "192.168.88.40"
targetp = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target,targetp))
client.send("GET / HTTP/1.1\r\nHost: 192.168.88.40\r\n\r\n")
response = client.recv(4096)

print response
