# Importing necessary modules
import hashlib
import socket
import hmac
import time

def vigenere_cipher(msg, ky, opt='Encrypt'):
    """
    Encrypt or decrypt a message using the Vigenere Cipher.

    Parameters:
    - msg: The message to be encrypted or decrypted.
    - ky: The key used for encryption or decryption.
    - opt: Specifies whether to 'Encrypt' or 'Decrypt'. Default is 'Encrypt'.

    Returns:
    - The result of encryption or decryption.
    """
    # Vigenere Cipher: A method of encrypting alphabetic text using a keyword
    # to perform polyalphabetic substitution.

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
            result += chr(((ord(char) - 97 + ((1 if opt == 'Encrypt' else -1) * (
                ord(new_ky[key_position % len(new_ky)]) - 48))) % 26) + 97)
            # Increment the key position
            key_position += 1
        else:
            # Retain non-alphabetic characters as is
            result += char
    return result

def hmac_calculation(msg, ky):
    """
    Calculate HMAC (Hash-based Message Authentication Code) for the given key and data.

    Parameters:
    - msg: The data for which HMAC is calculated.
    - ky: The key used for HMAC calculation.

    Returns:
    - The hexadecimal representation of the HMAC.
    """
    return hmac.new((ky.encode()), (str(msg).encode()), hashlib.sha256).hexdigest()

def serverside():
    """
    Server-side logic for handling connections and communication.
    """
    ip = 'localhost'
    port_number = 12345

    # Create a TCP IPv4 socket
    tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified IP and port
    tcp_ip4.bind((ip, port_number))

    # Listen for incoming connections
    tcp_ip4.listen()

    print("Waiting for a connection...")
    client_socket, client_address = tcp_ip4.accept()
    print(f"Connection established with {client_address}")

    while True:
        # Receive encrypted data and HMAC from the client
        received_encrypted_data = client_socket.recv(1024)
        received_hmac = client_socket.recv(64)

        if not received_encrypted_data:
            break

        # Check if the client wants to exit
        if vigenere_cipher(received_encrypted_data.decode(), str(port_number), opt='Decrypt') == 'exit':
            print("The Client wants to Exit the Server")
            break

        # Compute HMAC for verification
        computed_hmac = hmac_calculation((received_encrypted_data.decode()), str(port_number))

        if computed_hmac == (received_hmac.decode()):
            # Decrypt the data using the Vigenere cipher
            decrypted_data = vigenere_cipher((received_encrypted_data.decode()), str(port_number), opt='Decrypt')
            print('\nHMAC Verified. Client Message:', decrypted_data)

            # Sending a response back to the client
            response = str(input('Enter the Response from server: '))

            if response.lower() == 'exit':
                # Send 'exit' to the client to initiate exit process
                encrypted_exit_message = vigenere_cipher("exit", str(port_number))
                hmac_exit_message = hmac_calculation(encrypted_exit_message, str(port_number))

                client_socket.send(hmac_exit_message.encode())
                client_socket.send(encrypted_exit_message.encode())
                break  # End the conversation
            
            else:
                # Continue with normal response
                encrypted_response = vigenere_cipher(response, str(port_number))
                hmac_response = hmac_calculation(encrypted_response, str(port_number))

                client_socket.send(hmac_response.encode())
                client_socket.send((encrypted_response.encode()))

        else:
            print("HMAC verification failed.")

    client_socket.close()
    tcp_ip4.close()

def clientside():
    """
    Client-side logic for handling communication with the server.
    """
    ip = 'localhost'
    port_number = 12345

    # Create a TCP IPv4 socket
    tcp_ip4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    tcp_ip4.connect(('localhost', port_number))

    while True:
        # Sending data to the server
        data_to_send = input("\nEnter data to send to the server: ")

        if not data_to_send:
            break

        if data_to_send.lower() == 'exit':
            # Send 'exit' to the server to initiate exit process
            encrypted_exit_message = vigenere_cipher("exit", str(port_number))
            hmac_exit_message = hmac_calculation(encrypted_exit_message, str(port_number))

            tcp_ip4.send(encrypted_exit_message.encode())
            time.sleep(0.01)
            tcp_ip4.send(hmac_exit_message.encode())
            break

        encrypted_data_to_send = vigenere_cipher(str(data_to_send), str(port_number))
        hmac_to_send = hmac_calculation(encrypted_data_to_send, str(port_number))

        tcp_ip4.send(encrypted_data_to_send.encode())
        tcp_ip4.send(hmac_to_send.encode())

        # Receiving response from the server
        received_hmac_response = tcp_ip4.recv(64)
        received_encrypted_response = tcp_ip4.recv(1024)

        # Check if the server wants to exit
        if vigenere_cipher(received_encrypted_response.decode(), str(port_number), opt='Decrypt') == 'exit':
            print("The Server wants to Exit the Server")
            break

        # Decrypt the response using the Vigenere cipher
        decrypted_response = vigenere_cipher(received_encrypted_response.decode(), str(port_number), opt='Decrypt')
        computed_hmac_response = hmac_calculation(received_encrypted_response.decode(), str(port_number))

        if computed_hmac_response == received_hmac_response.decode():
            print("HMAC verified. Server response:", decrypted_response)
        else:
            print("HMAC verification failed.")

    tcp_ip4.close()

def start():
    print('This is a Chat-App Created Using Sockets.\nTo run this code, you need to run it in two separate terminals (or)\nYou can do one in VSCode and the other in the dedicated terminal.\n\nChoose which Side is this:\n1. Server Side\n2. Client Side')

    while True:
        try:
            ch = int(input('Enter Your Choice: '))
            if ch == 1:
                serverside()
                break
            elif ch == 2:
                clientside()
                break
            else:
                print('Invalid choice. Please enter 1 for Server Side or 2 for Client Side.')
        except ValueError:
            print('Invalid input. Please enter a valid choice (1 for Server Side or 2 for Client Side).')

start()