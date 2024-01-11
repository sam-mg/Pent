import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('127.0.0.1', 12345)  # Use localhost (127.0.0.1) and a port number
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server listening on {}:{}'.format(*server_address))

# Accept a connection
client_socket, client_address = server_socket.accept()
print('Connection established from {}:{}'.format(*client_address))

while True:
    # Receive data from the client
    data = client_socket.recv(1024)
    if not data:
        break
    print('Received from client:', data.decode())

    # Send a response back to the client
    response = input('Enter your response: ')
    client_socket.send(response.encode())

# Close the connection
client_socket.close()
server_socket.close()