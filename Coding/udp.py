# 1. A Socket is created using 'socket.socket()'
# 2. It is then binded to a address and port using 'socket.bind()'
# 3. There is no 'listen' and 'accept' here, it just waits for sending and recieving of data.
# 4. Data exchange takes place using 'socket.sendto()' or 'socket.recvfrom()'
# 5. At last if no longer needed, it is closed using 'socket.close()'

# Module for Socket Programming
import socket

# For IPv4
ip4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# For IPv6
ip6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)