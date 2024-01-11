import socket
import hashlib
import hmac

def vigenere_encrypt(key, data):
    encrypted = []
    key_str = str(key)
    key_length = len(key_str)
    for i in range(len(data)):
        key_char = ord(key_str[i % key_length])  # Convert key char to its ASCII value
        encrypted_char = (data[i] + key_char) % 256
        encrypted.append(encrypted_char)
    return bytes(encrypted)

def vigenere_decrypt(key, encrypted_data):
    decrypted = []
    key_str = str(key)
    key_length = len(key_str)
    for i in range(len(encrypted_data)):
        key_char = ord(key_str[i % key_length])  # Convert key char to its ASCII value
        decrypted_char = (encrypted_data[i] - key_char) % 256
        decrypted.append(decrypted_char)
    return bytes(decrypted)

def calculate_hmac(key, data):
    return hmac.new(str(key).encode(), data, hashlib.sha512).digest()

ip = 'localhost'
port_number = 12345

tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ip4.bind((ip, port_number))
tcp_ip4.listen()

print("Waiting for a connection...")
client_socket, client_address = tcp_ip4.accept()
print(f"Connection established with {client_address}")

while True:
    received_encrypted_data = client_socket.recv(1024)
    received_hmac = client_socket.recv(64)

    if not received_encrypted_data:
        break

    decrypted_data = vigenere_decrypt(port_number, received_encrypted_data)
    received_data = decrypted_data.decode('ascii', errors='ignore')
    computed_hmac = calculate_hmac(port_number, received_encrypted_data)

    if computed_hmac == received_hmac:
        print("HMAC verified. Received data:", received_data)
    else:
        print("HMAC verification failed.")

    # Sending a response back to the client
    response = b"Server received the data"
    encrypted_response = vigenere_encrypt(port_number, response)
    hmac_response = calculate_hmac(port_number, encrypted_response)

    client_socket.send(encrypted_response)
    client_socket.send(hmac_response)

# Indicate the end of communication
client_socket.send(b"END")
client_socket.close()
tcp_ip4.close()
