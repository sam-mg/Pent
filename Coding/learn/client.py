import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('127.0.0.1', 12345)  # Use the same address and port as the server
client_socket.connect(server_address)

while True:
    # Send a message to the server
    message = input('Enter your message: ')
    client_socket.send(message.encode())

    # Receive the response from the server
    data = client_socket.recv(1024)
    print('Received from server:', data.decode())

# Close the connection
client_socket.close()