import socket

s =socket.socket()

host = socket.gethostname()
port = 5100

s.connect((host,port))

while True:

	data = s.recv(1024)
	print "Other client sended following message : ", data
	if data == 'end':
		break
	data = raw_input('Enter data you want to send : ')
	s.sendall(data)
	print "Waiting for other client's reply!"
s.close()
