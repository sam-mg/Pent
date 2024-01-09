# Importing Modules
import hashlib
import socket
import hmac

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
    kp = 0
    
    # Iterate through each character in the message
    for char in msg:
        # Check if the character is alphabetic
        if char.isalpha():
            # Calculate the shift based on the key and perform encryption or decryption
            # Convert ASCII to integer
            # Encrypt or decrypt the character
            # Append the encrypted or decrypted character to the result
            result += chr(((ord(char) - 97 + ((1 if opt == 'Encrypt' else -1) * (ord(new_ky[kp % len(new_ky)]) - 48))) % 26) + 97)
            # Increment the key position
            k += 1  
        else:
            # Retain non-alphabetic characters as is
            result += char
    return result

def hashgenerate(data):
    # Calculate the SHA-512 hash of the text by encoding it as UTF-8 bytes,
    # Hashing using the hashlib library, and obtaining the hexadecimal digest.
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

def serverside():
    pass

def clientside():
    pass

print('This is a Chat-App Created Using Sockets.\nTo run this code, you need to run it in two seperate terminals (or)\nYou can do one in VSCode and other in the dedecated terminal.\n\nChoose which Side is this:\n1. Server Side\n2. Client Side')
ch = int(input('Enter Your Choice: '))

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
