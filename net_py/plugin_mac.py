import socket

target = "192.168.88.40"
targetp = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((target,targetp))
client.send("http://172.16.50.1/status")
response = client.recv(4096)

print response
