import socket

def main():
	host = "192.168.10.2"
	port = 4000

	s = socket.socket()
	s.connect((host,port))

	message = raw_input(':: ')
	while message != 'q':
		s.send(message)
		data = s.recv(1024)
		print 'Recieved from server ' + str(data)
		message = raw_input(':: ')
	s.close()

if __name__ == '__main__':
	main()
