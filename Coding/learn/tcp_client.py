# 1. A Socket is created using 'socket.socket()'
# 2. It is then binded to a address and port using 'socket.bind()'
# 3. It is then set for listenning to recieve connection from user/client using 'socket.listen()'
# 4. Once connection is made it is then accepted using 'socket.accept()'
# 5. Data exchange takes place using 'socket.send()' or 'socket.recv()'
# 6. At last if no longer needed, it is closed using 'socket.close()'

# Module for Socket Programming
import socket

# For IPv4
tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# For IPv6
#tcp_ip6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# It is then connected to the server address and port using 'socket.connect()'
# Specify the server's address and port to establish a connection
# Replace <server_port> with the actual port number
server_address = ('localhost', '<server_port>')
tcp_client.connect(server_address)

# To send data
# The data has to be encoded (Converted into bytes) since it transfers only binary data
data_to_send = '<The_Data>'
tcp_client.send(data_to_send.encode())

# To receive data
# Specify the maximum amount of data to be received at once (in bytes)
received_data = tcp_client.recv(1024).decode()
# You can print 'received_data' to view the received data

# To close
tcp_client.close()