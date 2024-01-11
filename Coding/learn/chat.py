# Importing Modules
import hashlib
import socket
import hmac
import os


def vigenere_cipher(msg, ky, opt='Encrypt'):
    # We are using Vigenere Cipher
    # A method of encrypting alphabetic text using a keyword to perform polyalphabetic substitution.

    # Convert the message to lowercase
    msg = msg.lower()
    
    # Generate a key that matches the length of the message
    new_ky = str(ky) * ((len(msg) // len(str(ky))) + 1)

    # Final Text (Encryption or Decryption)
    result = ''

    # Key Position
    key_position = 0
    
    # Iterate through each character in the message
    for char in msg:
        # Check if the character is alphabetic
        if char.isalpha():
            # Calculate the shift based on the key and perform encryption or decryption
            # Convert ASCII to integer
            # Encrypt or decrypt the character
            # Append the encrypted or decrypted character to the result
            result += chr(((ord(char) - 97 + ((1 if opt == 'Encrypt' else -1) * (ord(new_ky[key_position % len(new_ky)]) - 48))) % 26) + 97)
            # Increment the key position
            key_position += 1  
        else:
            # Retain non-alphabetic characters as is
            result += char
    return result

def hashgenerate(data):
    # Calculate the SHA-512 hash of the text by encoding it as UTF-8 bytes,
    # Hashing using the hashlib library, and obtaining the hexadecimal digest.
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

def calculate_hmac(key, data):
    return hmac.new(str(key).encode(), data.encode(), hashlib.sha256).hexdigest()

def serverside():
    ip = 'localhost'
    port_number = 12345

    tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_ip4.bind((ip, port_number))
    tcp_ip4.listen()

    print("Waiting for a connection...")
    client_socket, client_address = tcp_ip4.accept()
    print(f"Connection established with {client_address}")

    try:
        while True:
            received_encrypted_data = client_socket.recv(1024)
#            received_hmac = client_socket.recv(64)

            if not received_encrypted_data:
                break

            decrypted_data = vigenere_cipher((received_encrypted_data.decode()), str(port_number), opt='Decrypt')
            received_data = decrypted_data
            print(received_data)
#            computed_hmac = calculate_hmac(port_number, received_encrypted_data)

            # if computed_hmac == received_hmac:
            #     print("HMAC verified. Received data:", received_data)
            # else:
            #     print("HMAC verification failed.")

            # Sending a response back to the client
            response = "Server received the data"
            encrypted_response = vigenere_cipher(response, str(port_number))
#            hmac_response = calculate_hmac(port_number, encrypted_response)

            client_socket.send((encrypted_response.encode()))
#            client_socket.send(hmac_response)
    finally:
        # Indicate the end of communication
        client_socket.send(b"END")
        client_socket.close()
        tcp_ip4.close()


def clientside():
    ip = 'localhost'
    port_number = 12345

    tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_ip4.connect(('localhost', port_number))

    try:
        while True:
            # Sending data to the server
            data_to_send = input("Enter data to send to server: ")
            if not data_to_send:
                break

            # Ensure data_to_send is a string and then encode
            data_to_send = str(data_to_send)
            encrypted_data_to_send = vigenere_cipher(data_to_send, str(port_number))
#            hmac_to_send = calculate_hmac(port_number, encrypted_data_to_send)

            tcp_ip4.send((encrypted_data_to_send).encode())
#            tcp_ip4.send(hmac_to_send)

            # Receiving response from the server
            received_encrypted_response = tcp_ip4.recv(1024)
            received_hmac_response = tcp_ip4.recv(64)

            decrypted_response = vigenere_cipher((received_encrypted_response.decode()), str(port_number), opt='Decrypt')
#            computed_hmac_response = calculate_hmac(port_number, received_encrypted_response)

            # if computed_hmac_response == received_hmac_response:
            #     print("HMAC verified. Server response:", decrypted_response.decode('latin-1'))
            # else:
            #     print("HMAC verification failed.")

            print("Server response:", decrypted_response)
    finally:
        tcp_ip4.close()

def option():
    # Clearing the Screen
    if os.name == 'nt':  # Check if the operating system is Windows
        os.system('cls')
    else:  # Assume Unix-based system
        os.system('clear')
    print('This is a Chat-App Created Using Sockets.\nTo run this code, you need to run it in two separate terminals (or)\nYou can do one in VSCode and other in the dedicated terminal.\n\nChoose which Side is this:\n1. Server Side\n2. Client Side')
    ch = int(input('Enter Your Choice: '))
    return ch

while True:
    try:
        ch = option()
        if ch == 1:
            serverside()
            break
        elif ch == 2:
            clientside()
            break
        else:
            print('Invalid choice.')
            option()
    except ValueError:
        print('Invalid input. Please enter a valid choice (1 for Server Side or 2 for Client Side).')
        option()