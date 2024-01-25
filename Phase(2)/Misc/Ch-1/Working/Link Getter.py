import base64

encrypted_data = 'aHR0cHM6Ly9naXN0LmdpdGh1Yi5jb20vclNyaWtlc2gvY2NiY2NjNjIyMmU4NTdlNDI2ZTUzYjJjNzk1NmJlMGE='

decoded_data = base64.b64decode(encrypted_data)
print(f'Decoded Message: {decoded_data.decode("utf-8", "ignore")}')