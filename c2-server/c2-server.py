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
	clientsocket, client_ip = s.accept()
	print("[+] received a connection from -> {}".format(client_ip))

	encoded_data = clientsocket.recv(4096)
	print("[+] received data: {}".format(encoded_data))  # Print the received data
	clientsocket.close()

	random_file_name = "".join(random.choices(ascii_lowercase, k = 10))
	print("[+] writing data to file: {}".format(random_file_name))  # Print the name of the file being written to

	random_fd = open(random_file_name, "wb")
	try:
		decoded_data = base64.b64decode(encoded_data).decode("UTF-8")
		print("[+] decoded data: {}".format(decoded_data))  # Print the decoded data
		random_fd.write(decoded_data)
	except UnicodeDecodeError as e:
		print("[-] UnicodeDecodeError: ", e)
		print("[-] Data causing the error: ", encoded_data)
	finally:
		random_fd.close()
		print("[+] file closed")  # Print a message after the file has been closed

	print("[+] data written to file and file closed")  # Print a message after the file has been written and closed