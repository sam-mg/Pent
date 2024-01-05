# 1. A Socket is created using 'socket.socket()'
# 2. It is then binded to a address and port using 'socket.bind()'
# 3. There is no 'listen' and 'accept' here, it just waits for sending and recieving of data.
# 4. Data exchange takes place using 'socket.sendto()' or 'socket.recvfrom()'
# 5. At last if no longer needed, it is closed using 'socket.close()'

# Module for Socket Programming
import socket

# For IPv4
udp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# For IPv6
#udp_ip6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

# For Binding with the same computer
udp_ip4p_ip4.bind('localhost', '<number between 0 to 65535 preferebaile above 1024>')
# For a different computer
udp_ip4.bind('<ip address>', '<number between 0 to 65535 preferebaile above 1024>')

# No 'listen' nor 'accept'
# Just sending and recieving of data

# To send data
# The data has to be encoded (Converted into bytes)
# Since it transfers only binary data
# The data is sent to the specific address
udp_ip4.sendto('<The_Data>'.encode(), ('localhost', 'port_number'))

# To recieve data
# We reciecve two things
# 1) Data
# 2) The address from where the data is sent
data, address = udp_ip4.recvfrom(1024)
# To view the data, just decode() and print it

# To close
tcp_ip4.close()