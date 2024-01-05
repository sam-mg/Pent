# 1. A Socket is created using 'socket.socket()'
# 2. It is then binded to a address and port using 'socket.bind()'
# 3. It is then set for listenning to recieve connection from user/client using 'socket.listen()'
# 4. Once connection is made it is then accepted using 'socket.accept()'
# 5. Data exchange takes place using 'socket.send()' or 'socket.recv()'
# 6. At last if no longer needed, it is closed using 'socket.close()'

# Module for Socket Programming
import socket

# For IPv4
ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# For IPv6
ip6 = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)