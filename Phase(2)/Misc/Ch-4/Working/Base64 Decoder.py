import base64

def decrypt_and_print_data(file_path):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    target_iterations = 36  # Set the desired number of iterations
    loop_count = 0  # Initialize loop counter

    while loop_count < target_iterations:
        loop_count += 1  # Increment loop counter
        try:
            decoded_data = base64.urlsafe_b64decode(encrypted_data)
        except base64.binascii.Error:
            # Add padding if decoding fails
            encrypted_data += b'=' * (4 - (len(encrypted_data) % 4))
        else:
            if loop_count == 34 or loop_count == 35 or loop_count == 36:
                print("Iteration:", loop_count, "Decoded data:", decoded_data)

            if decoded_data.endswith(b"}"):
                print("Number of loop iterations:", loop_count)
                break
            else:
                encrypted_data = decoded_data

    try:
        decrypted_data = decoded_data.decode("utf-8")  # Assuming text data
        print("Decrypted data:", decrypted_data)
    except UnicodeDecodeError:
        print("Error decoding data. It might not be text-based.")

# Replace the file path with your actual file path
file_path = "/Users/sammgharish/Desktop/Pent/Phase(2)/Misc/Ch-4/Org File/msg.txt"

# Call the function with the specified file path
decrypt_and_print_data(file_path)
