import socket
import hashlib
import hmac

def vigenere_encrypt(key, data):
    encrypted = []
    key_str = str(key)
    key_length = len(key_str)
    for i in range(len(data)):
        key_char = key_str[i % key_length]
        encrypted_char = (data[i] + ord(key_char)) % 256
        encrypted.append(encrypted_char)
    return bytes(encrypted)

def vigenere_decrypt(key, encrypted_data):
    decrypted = []
    key_str = str(key)
    key_length = len(key_str)
    for i in range(len(encrypted_data)):
        key_char = key_str[i % key_length]
        decrypted_char = (encrypted_data[i] - ord(key_char)) % 256
        decrypted.append(decrypted_char)
    return bytes(decrypted)

def calculate_hmac(key, data):
    return hmac.new(str(key).encode(), data, hashlib.sha512).digest()

port_number = 12345

tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_ip4.connect(('localhost', port_number))

while True:
    # Sending data to the server
    data_to_send = input("Enter data to send to server: ").encode()
    if not data_to_send:
        break

    encrypted_data_to_send = vigenere_encrypt(port_number, data_to_send)
    hmac_to_send = calculate_hmac(port_number, encrypted_data_to_send)

    tcp_ip4.send(encrypted_data_to_send)
    tcp_ip4.send(hmac_to_send)

    # Receiving response from the server
    received_encrypted_response = tcp_ip4.recv(1024)
    received_hmac_response = tcp_ip4.recv(64)

    decrypted_response = vigenere_decrypt(port_number, received_encrypted_response)
    computed_hmac_response = calculate_hmac(port_number, received_encrypted_response)

    if computed_hmac_response == received_hmac_response:
        print("HMAC verified. Server response:", decrypted_response.decode('latin-1'))
    else:
        print("HMAC verification failed.")

tcp_ip4.close()