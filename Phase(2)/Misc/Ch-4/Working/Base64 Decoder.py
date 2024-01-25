import base64

def decoder(data):
    return base64.b64decode(data)

encrypted_data = open('/Users/sammgharish/Desktop/Pent/Phase(2)/Misc/Ch-4/Org File/msg.txt', "rb").read()

for i in range(50):
    decoded_data = decoder(encrypted_data)
    
    if not decoded_data or decoded_data.isspace():
        print('All Done\nIt Ended in', i + 1)
        break

    print(f'Times: {i + 1}\nDecoded Message: {decoded_data.decode("utf-8", "ignore")}')
    encrypted_data = decoded_data