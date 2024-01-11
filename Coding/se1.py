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

def server_program():
    host = 'localhost'
    port = 10001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("Received: " + plainText(str(data), key))
        data = input(' -> ')
        conn.send(cipherText(data, key).encode())

    conn.close()


if __name__ == '__main__':
    server_program()