# This Python script sets up a simple TCP server that listens for incoming connections 
# and receives data from them. 

#!/usr/bin/python3
import socket
import base64
import random
from string import ascii_lowercase

# create TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# listen on localhost port 1337
s.bind(("127.0.0.1", 1337))

# queue up to 5 requests
s.listen(5)

print("listening on port 1337...")

# This line starts an infinite loop, meaning the server will 
# continue to accept connections until it is manually stopped
while True:
	# establish a connection
	clientsocket, client_ip = s.accept()
	print("[+] received a connection from -> {}".format(client_ip))

	# get the encoded data
	# This line receives up to 4096 bytes of data from the client
	encoded_data = clientsocket.recv(4096)
	clientsocket.close()

	# open a file with a random name and insert the decoded data into it
	random_fd = open("".join(random.choices(ascii_lowercase, k = 10)), "wb")  # Open the file in binary mode
	random_fd.write(base64.b64decode(encoded_data))  # Write the decoded base64 data directly to the file
	# This line closes the connection to the client
	random_fd.close()