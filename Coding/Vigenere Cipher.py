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

#message = "Hello World!!"
#key = 1234
message = str(input('Enter the String: '))
key = int(input('Enter the Key: '))

encrypted_text = vigenere_cipher(message, key)
decrypted_text = vigenere_cipher(encrypted_text, key, opt='Decrypt')

print("Original message:", message)
print("Encrypted message:", encrypted_text)
print("Decrypted message:", decrypted_text)
