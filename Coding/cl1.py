import socket

key = "I will kill you"

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)

def plainText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)

def client_program():
    host = 'localhost'
    port = 10001

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input(" -> ")
        encrypted = cipherText(message, key)

        client_socket.send(encrypted.encode())
        data = client_socket.recv(1024).decode()

        print('Received: ' + plainText(data, key))

        if message.lower().strip() == 'bye':
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()


if __name__ == '__main__':
    client_program()