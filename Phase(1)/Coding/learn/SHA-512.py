import hashlib

def sha512_hash(text):
    return hashlib.sha512(text.encode('utf-8')).hexdigest()

# Example usage:
text = "Hello, this is a string to hash?"
hashed_text = sha512_hash(text)
print("Original text:", text)
print("SHA-512 Hash:", hashed_text)
