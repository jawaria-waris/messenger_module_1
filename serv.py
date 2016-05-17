import socket
import sys
from thread import *

HOST = ''  # Symbolic name meaning all available interfaces
PORT = 5100  # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

# Start listening on socket
s.listen(10)
print 'Socket now listening'

# Function for handling connections. This will be used to create threads
def clientthread(client1,client2):
	while True:

		# Receiving from client
			data = client1.recv(1024)
			client2.sendall(data)
			data = client2.recv(1024)
			client1.sendall(data)
	client1.close()
	client2.close()
# now keep talking with the client
while 1:
    # wait to accept a connection - blocking call
    client1, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    client2, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread, (client1,client2))

s.close()

