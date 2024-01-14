# Importing necessary modules
import hashlib
import socket
import hmac
import time

def vigenere_cipher(message, key, operation='Encrypt'):
    """
    Encrypts or decrypts a message using the Vigenere Cipher.

    Parameters:
    - message: The message to be encrypted or decrypted.
    - key: The key used for encryption or decryption.
    - operation: Specifies whether to 'Encrypt' or 'Decrypt'. Default is 'Encrypt'.

    Returns:
    - The result of encryption or decryption.
    """
    # Vigenere Cipher: A method of encrypting alphabetic text using a keyword
    # to perform polyalphabetic substitution.

    # Convert the message to lowercase
    message = message.lower()

    # Generate a key that matches the length of the message
    extended_key = str(key) * ((len(message) // len(str(key))) + 1)

    # Final Text (Encryption or Decryption)
    result = ''

    # Key Position
    key_position = 0

    # Iterate through each character in the message
    for char in message:
        # Check if the character is alphabetic
        if char.isalpha():
            # Calculate the shift based on the key and perform encryption or decryption
            # Convert ASCII to integer
            # Encrypt or decrypt the character
            # Append the encrypted or decrypted character to the result
            result += chr(((ord(char) - 97 + ((1 if operation == 'Encrypt' else -1) * (
                ord(extended_key[key_position % len(extended_key)]) - 48))) % 26) + 97)
            # Increment the key position
            key_position += 1
        else:
            # Retain non-alphabetic characters as is
            result += char
    return result

def hmac_calculation(data, key):
    """
    Calculates HMAC (Hash-based Message Authentication Code) for the given key and data.

    Parameters:
    - data: The data for which HMAC is calculated.
    - key: The key used for HMAC calculation.

    Returns:
    - The hexadecimal representation of the HMAC.
    """
    return hmac.new((key.encode()), (str(data).encode()), hashlib.sha512).hexdigest()

def serverside():
    """
    Server-side logic for handling connections and communication.
    """
    server_ip = 'localhost'
    server_port = 12345

    # Create a TCP IPv4 socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified IP and port
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen()

    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    while True:
        # Receive encrypted data and HMAC from the client
        received_encrypted_data = client_socket.recv(1024)
        received_hmac = client_socket.recv(128)

        if not received_encrypted_data:
            break

        # Check if the client wants to exit
        if vigenere_cipher(received_encrypted_data.decode(), str(server_port), operation='Decrypt') == 'exit':
            print("The Client wants to Exit the Chat")
            break

        # Compute HMAC for verification
        computed_hmac = hmac_calculation((received_encrypted_data.decode()), str(server_port))

        if computed_hmac == (received_hmac.decode()):
            # Decrypt the data using the Vigenere cipher
            decrypted_data = vigenere_cipher((received_encrypted_data.decode()), str(server_port), operation='Decrypt')
            print('\nHMAC Verified. Client Message:', decrypted_data)

            # Sending a response back to the client
            response = str(input('Enter the Response from server: '))

            if response.lower() == 'exit':
                # Send 'exit' to the client to initiate exit process
                encrypted_exit_message = vigenere_cipher("exit", str(server_port))
                hmac_exit_message = hmac_calculation(encrypted_exit_message, str(server_port))

                client_socket.send(hmac_exit_message.encode())
                time.sleep(0.01)
                client_socket.send(encrypted_exit_message.encode())
                break  # End the conversation
            
            else:
                # Continue with normal response
                encrypted_response = vigenere_cipher(response, str(server_port))
                hmac_response = hmac_calculation(encrypted_response, str(server_port))

                client_socket.send(hmac_response.encode())
                time.sleep(0.01)
                client_socket.send((encrypted_response.encode()))

        else:
            print("HMAC verification failed.")

    client_socket.close()
    server_socket.close()

def clientside():
    """
    Client-side logic for handling communication with the server.
    """
    server_ip = 'localhost'
    server_port = 12345

    # Create a TCP IPv4 socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, server_port))

    while True:
        # Sending data to the server
        data_to_send = input("\nEnter data to send to the server: ")

        if not data_to_send:
            break

        if data_to_send.lower() == 'exit':
            # Send 'exit' to the server to initiate exit process
            encrypted_exit_message = vigenere_cipher("exit", str(server_port))
            hmac_exit_message = hmac_calculation(encrypted_exit_message, str(server_port))

            client_socket.send(encrypted_exit_message.encode())
            time.sleep(0.01)
            client_socket.send(hmac_exit_message.encode())
            break

        encrypted_data_to_send = vigenere_cipher(str(data_to_send), str(server_port))
        hmac_to_send = hmac_calculation(encrypted_data_to_send, str(server_port))

        client_socket.send(encrypted_data_to_send.encode())
        client_socket.send(hmac_to_send.encode())

        # Receiving response from the server
        received_hmac_response = client_socket.recv(128)
        received_encrypted_response = client_socket.recv(1024)

        # Check if the server wants to exit
        if vigenere_cipher(received_encrypted_response.decode(), str(server_port), operation='Decrypt') == 'exit':
            print("The Server wants to Exit the Chat")
            break

        # Decrypt the response using the Vigenere cipher
        decrypted_response = vigenere_cipher(received_encrypted_response.decode(), str(server_port), operation='Decrypt')
        computed_hmac_response = hmac_calculation(received_encrypted_response.decode(), str(server_port))

        if computed_hmac_response == received_hmac_response.decode():
            print("HMAC verified. Server response:", decrypted_response)
        else:
            print("HMAC verification failed.")

    client_socket.close()

def start():
    print('This is a Chat-App Created Using Sockets.\nTo run this code, you need to run it in two separate terminals (or)\nYou can do one in VSCode and the other in the dedicated terminal.\n\nChoose which Side is this:\n1. Server Side\n2. Client Side')

    while True:
        try:
            user_choice = int(input('Enter Your Choice: '))
            if user_choice == 1:
                serverside()
                break
            elif user_choice == 2:
                clientside()
                break
            else:
                print('Invalid choice. Please enter 1 for Server Side or 2 for Client Side.')
        except ValueError:
            print('Invalid input. Please enter a valid choice (1 for Server Side or 2 for Client Side).')

start()