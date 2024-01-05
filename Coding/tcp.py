# 1. A Socket is created using 'socket.socket()'
# 2. It is then binded to a address and port using 'socket.bind()'
# 3. It is then set for listenning to recieve connection from user/client using 'socket.listen()'
# 4. Once connection is made it is then accepted using 'socket.accept()'
# 5. Data exchange takes place using 'socket.send()' or 'socket.recv()'
# 6. At last if no longer needed, it is closed using 'socket.close()'

# Module for Socket Programming
import socket

# For IPv4
tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# For IPv6
#tcp_ip6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# For Binding with the same computer
tcp_ip4.bind('localhost', '<number between 0 to 65535 preferebaile above 1024>')
# For a different computer
tcp_ip4.bind('<ip address>', '<number between 0 to 65535 preferebaile above 1024>')

# After binding we need to wait for user/client
tcp_ip4.listen()

# Accepting a connection
# Return two values
# 1) Socket between Server and client alone
# 2) Client's IP and port
client_socket, client_address = tcp_ip4.accept()

# To send data
# The data has to be encoded (Converted into bytes)
# Since it transfers only binary data
client_socket.send('<The_Data>'.encode())

# To recieve data
recieved_data = client_socket.recv(1024).decode()
# You can just print 'recieved_data' to view it

# To close
tcp_ip4.close()