import hashlib

data = "Hello, this is some data to hash"

data_bytes = data.encode()
sha512_hash = hashlib.sha512()
sha512_hash.update(data_bytes)
hashed_data = sha512_hash.hexdigest()

print("SHA-512 Hash:", hashed_data)